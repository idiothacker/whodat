# whodat.py
whodat.py is a simple python script that will take either a single domain or a line delimited list of domains, query them against the whois database, and then write the results to a CSV output file.

## Installation
Clone the repository, navigate into the `whodat` folder and then run the following command.

``` python
pip install -r requirements.txt
```

## How to Use
Simply pass the script to python, providing either the `-d` (single domain) or `-D` (domain list) and the `-o` (output file) flags, providing your own values.

### Single Domain Example:
``` bash
python whodat.py -d google.com -o "C:\whois\google.csv"
```

### Domain List Example:
``` bash
python whodat.py -D "C:\whois\domains.txt" -o "C:\whois\results.csv"
```

### Help (-h):
``` bash
usage: whodat.py [-h] [-d --domain] [-D --domain_file] -o --outfile_file

Whodat will query the Whois database for the provided domain(s), and save the results in CSV fromat.

optional arguments:
  -h, --help         show this help message and exit
  -d --domain        A single domain to query. (example.com)
  -D --domain_file   The location of a domain list file, 1 domain per line. ("C:\whois\domains.txt")
  -o --outfile_file  The location and name of the output file ("C:\whois\results.csv")
```