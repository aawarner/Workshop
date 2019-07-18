from requests import request, packages
from json import dumps,loads
from requests.auth import HTTPBasicAuth
from sys import exit,argv
from getpass import getpass

packages.urllib3.disable_warnings()

def read_csv(filename):
    '''aquire interface config data from a CSV file'''
    with open (filename,'r') as f:
        rl=f.readlines()
        array=[i.rstrip('\n').split(',') for i in rl]
    return array

def int_cfg(int_name,ip,netmask,description,enabled,type):
    '''return individual interface config'''
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

def merge_missing_data(payload_json,device,username,password):
    '''compares GET data with config data from CSV file and merges interfaces not present'''
    url = "https://%s/restconf/data/ietf-interfaces:interfaces/"%device
    headers = {'Accept': "application/yang-data+json",'Content-Type': "application/yang-data+json"}
    response = request("GET", url, headers=headers, auth=HTTPBasicAuth(username, password), verify=False)
    get_int_json=response.json()
    missing_index_list=[]
    get_ints=[i["name"] for i in get_int_json["ietf-interfaces:interfaces"]["interface"]]
    cfg_ints=[i["name"] for i in payload_json["ietf-interfaces:interfaces"]["interface"]]
    for i in get_ints:
        if i not in cfg_ints:
            missing_index_list.append(get_ints.index(i))
    for i in missing_index_list:
        payload_json["ietf-interfaces:interfaces"]["interface"].insert(i,get_int_json["ietf-interfaces:interfaces"]["interface"][i])
    print(dumps(payload_json,indent=2))
    payload=dumps(payload_json)
    return payload,payload_json

def put_intf_cfg (filename, device, username, password, delete=False):
    '''send a PUT to the specified device with the payload data derived from the CSV'''
    array=read_csv(filename)
    payload,payload_json=build_payload(array)
    if delete == False:
        payload,payload_json=merge_missing_data(payload_json,device,username,password)
    url = "https://%s/restconf/data/ietf-interfaces:interfaces/"%device
    headers = {'Accept': "application/yang-data+json",'Content-Type': "application/yang-data+json"}
    response = request("PUT", url, data=payload, headers=headers, auth=HTTPBasicAuth(username, password), verify=False)
    print(response.text)

if __name__ == "__main__":
    try:
        skip,filename,device,username,*trash=argv
        password=getpass("\nInput Password for %s on device %s: "%(username,device))
    except:
        print('\nexample syntax: #> python csv_exercise.py interfaces.csv csr admin\n')
        filename,device,username,password=('interfaces.csv','csr','admin','cisco123')

    delete_var=input("Delete interfaces not present in CSV? (y/n) :  ")
    if delete_var.lower() == 'y':
        delete_var=True
    else:
        delete_var=False
    put_intf_cfg(filename,device,username,password,delete_var)
