from requests import request, packages
from json import dumps,loads
from requests.auth import HTTPBasicAuth
from sys import exit,argv
from getpass import getpass

packages.urllib3.disable_warnings()

def read_csv(filename):
    '''1. aquire interface config data from a CSV file, using function from previous exercise'''

    return array

def int_cfg(int_name,ip,netmask,description,enabled,type):
    '''return individual interface config, use this to build 'int_list' '''
    intf={"name": int_name,"description": description,"type": type,"enabled": enabled,"ietf-ip:ipv4": {"address": [{"ip": ip,"netmask": netmask}]},"ietf-ip:ipv6": {}}
    return intf

def normalize_elements(int_name,enabled):
    '''normalizes interface names, types, and state into API expected JSON format'''
    int_number=max([i for i in list(range(65535)) if str(i) in int_name])
    if int_name.startswith('gi')  or int_name.startswith('Gi')  or int_name.startswith('GI'):
        int_type='GigabitEthernet'
        type="iana-if-type:ethernetCsmacd"
    elif 'lo' in int_name or 'Li' in int_name or 'LO' in int_name:
        int_type='Loopback'
        type="iana-if-type:softwareLoopback"
    else:
        print("\n\n***Unsupported Interface Type: %s***\n\n"%int_name)
        exit()

    int_name=int_type+str(int_number)

    if 'no' in enabled or 'NO' in enabled or 'NO' in enabled:
        enabled=True
    else:
        enabled=False

    return int_name,enabled,type

def build_payload(array):
    '''builds payload to be used in request operation by building list of individual interface configs'''
    int_list=[]
    for i in array:
        int_name, ip, netmask, description, enabled = i
        int_name, enabled, type = normalize_elements(int_name,enabled)
        intf=int_cfg(int_name,ip,netmask,description,enabled, type)
        int_list.append(intf)
    payload_json={"ietf-interfaces:interfaces": {"interface": int_list}}
    payload=dumps(payload_json)
    return payload,payload_json


def main(filename):
    '''2. build a main function that uses the sample requests code below to PUT the interface config to the CSR while
    using the previously functions'''

    '''SAMPLE CODE: url = "https://%s/restconf/data/ietf-interfaces:interfaces/"%device
    headers = {'Accept': "application/yang-data+json",'Content-Type': "application/yang-data+json"}
    response = request("PUT", url, data=payload, headers=headers, auth=HTTPBasicAuth(username, password), verify=False)
    print(response.text)'''

if __name__ == "__main__":
    '''3. call your main function and verify results'''
