'''
Using the SDWAN vManage API documentation write a Python program that
will gather the device information for all SDWAN devices in the fabric.
Print only the Hostname, System IP, Device ID, Device Model, UUID, and Site ID
for each device to your console.

BONUS!!!
Use the tabulate library to print your results in to a table.
'''

import requests
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from tabulate import tabulate
import sys

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

vmanage = "18.233.17.52"

url = "https://" + vmanage + "/dataservice/device"

headers = {"content-type": "application/json", "Accept": "application/json"}

username = "admin"
password = "admin"

try:
    response = requests.get(
        url,
        headers=headers,
        auth=HTTPBasicAuth(username, password),
        timeout=10,
        verify=False,
    )

except requests.exceptions.RequestException as e:
    print(e)
    sys.exit()

try:
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("Error: " + str(e))
    sys.exit()


code = response.status_code
response_json = response.json()

print("#" * 80)
print("API Response Code: %i \nURI: %s" % (code, url))
print("\nGetting list of SDWAN vEdge's from vManage: \n")

table = []
headers_dict = {
    "Host Name": "host-name",
    "System IP": "system-ip",
    "Device ID": "deviceId",
    "Device Model": "device-model",
    "SDWAN UUID": "uuid",
    "Site ID": "site-id"
}
headers = [i for i in headers_dict.keys()]
for event in response_json["data"]:
    tr = []
    for i in headers:
        try:
            tr.append(event[headers_dict[i]])
        except:
            tr.append("N/A")
            pass
    table.append(tr)
print(tabulate(table, headers=headers, tablefmt="fancy_grid"))
print()
