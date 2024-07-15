import os
import requests
import pyexcel_ods3
import csv
import time
from bs4 import BeautifulSoup

# Define colors for console output
NC = "\033[0m"
GR = "\033[0;32m"
YL = "\033[0;33m"
CY = "\033[0;36m"

# File paths
ods_file = "Scope.ods"
csv_file = "Scope.csv"
domains_file = "domains.txt"

# Clean up any existing files
for file in [ods_file, csv_file, domains_file]:
    if os.path.exists(file):
        os.remove(file)

# Fetch the URL of the ODS file
response = requests.get("https://www.communicatierijk.nl/vakkennis/r/rijkswebsites/verplichte-richtlijnen/websiteregister-rijksoverheid")
response.raise_for_status()
soup = BeautifulSoup(response.content, 'html.parser')
ods_link = None

for link in soup.find_all('a', href=True):
    if link['href'].endswith('.ods'):
        ods_link = link['href']
        break

if not ods_link:
    raise ValueError("ODS file link not found on the webpage")
    
url = "https://www.communicatierijk.nl" + ods_link

print(f"FILE PATH:{CY} {url} {NC}")

# Download the ODS file
response = requests.get(url)
with open(ods_file, 'wb') as file:
    file.write(response.content)

# Convert ODS to CSV using pyexcel-ods3
data = pyexcel_ods3.get_data(ods_file)
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for sheet in data.values():
        for row in sheet:
            writer.writerow(row)

# Process CSV to extract subdomains
with open(csv_file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    subdomains = {row[0].split("//")[-1].split("/")[0].split(":")[0] for row in reader if row}

# Remove first two entries, sort, and get unique subdomains
subdomains = sorted(subdomains)[2:]
unique_subdomains = sorted(set(subdomains), key=subdomains.index)

# Write to domains file
with open(domains_file, 'w') as file:
    for subdomain in unique_subdomains:
        if subdomain.count('.') > 1:
            subdomain = '.'.join(subdomain.split('.')[1:])
        file.write(f"{subdomain}\n")

# Print results
time.sleep(2)
print()
print(f"Total number of subdomains found:{GR} {len(unique_subdomains)} {NC}\n")
print(f"The list of In-Scope domains are saved in:{YL} {os.getcwd()}/{domains_file} {NC}\n")
