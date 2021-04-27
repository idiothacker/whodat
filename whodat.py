import whois, argparse, csv

parser = argparse.ArgumentParser(description="Whodat will query the Whois database for the provided domain(s), and save the results in CSV fromat.")
parser.add_argument("-d", metavar="--domain", help="A single domain to query. (example.com)")
parser.add_argument("-D", metavar="--domain_file", help="The location of a domain list file, 1 domain per line. (\"C:\\whois\\domains.txt\")")
parser.add_argument("-o", metavar="--outfile_file", help="The location and name of the output file (\"C:\\whois\\results.csv\")", required=True)

args = parser.parse_args()
in_file = args.D
domain = args.d
out_file = args.o

# Performs the whois query, parses the data, and returns a dictionary that is ready to be written to the csv
def query_whois(d):
    w = whois.whois(d)
    statuses = []
    servers = []
    res = {
        "Domain": d,
        "Status": "",
        "Transfer Lock": "No",
        "Creation Date": str(w.creation_date[0]).split(" ")[0],
        "Update Date": str(w.updated_date[0]).split(" ")[0],
        "Experation Date": str(w.expiration_date[0]).split(" ")[0],
        "Name Servers": ""
    }
    
    # Parse the statuses into unique values
    for s in w.status:
        if s.split(" ")[0] not in statuses:
            statuses.append(s.split(" ")[0])
    
    # Write the statuses to the return dictionary
    for s in statuses:
         res["Status"] = res["Status"] + s
         if s != statuses[-1]:
             res["Status"] = res["Status"] + "\n"
        # Set the Transfer Lock to "Yes" in the return dictionary if the domain is locked
         if s == "clientTransferProhibited" or s == "serverTransferProhibited":
             res["Transfer Lock"] = "Yes"
    
    # Create list of unique name servers
    for ns in w.name_servers:
        if ns.lower() not in servers:
            servers.append(ns.lower())
    
    # Write name servers to return dictionary
    for ns in servers:
        res["Name Servers"] = res["Name Servers"] + ns
        if ns != servers[-1]:
            res["Name Servers"] = res["Name Servers"] + "\n"
    
    return res

if args.d == None and args.D == None:
    print("You must provide a domain or a list of domains. Use the -h argument for more details.")
    quit()

with open(out_file, "w", newline="") as csvfile:
    fieldnames = ["Domain", "Status", "Transfer Lock", "Creation Date", "Update Date", "Experation Date","Name Servers"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)   
    writer.writeheader() 
    
    if domain != None:
        res = query_whois(domain)
        writer.writerow(res)
