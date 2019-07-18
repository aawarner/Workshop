'''
EXERCISE:

Write a program that will log in to your CSR1000v and deploy the below access-list.
Changes should be written to a file called changes.txt.


ip access-list extended python_acl
 remark ACL added by Python
 permit ip any host 1.2.3.4
 permit ip host 1.2.3.4 any
 deny ip any any

 BONUS:

 After deploying the ACL download the startup config and the running config and write them to a file.
 Compare the two files and write the differences to your console.

 HINT!!!
 Use python library difflib to compare the files and print the differences to your console.
'''

import netmiko
import difflib

# Netmiko define device
csr = {
    'ip': '10.10.10.145',
    'device_type': 'cisco_ios',
    'username': 'cisco',
    'password': 'cisco',
}

# Netmiko config set
configs = ['ip access-list extended python_acl', 'remark ACL added by Python', 'permit ip any host 1.2.3.4',
           'permit ip host 1.2.3.4 any', 'deny ip any any']

# Establish SSH session via Netmiko
try:
    conn = netmiko.ConnectHandler(**csr)
except (netmiko.NetMikoTimeoutException, netmiko.NetMikoAuthenticationException,) as e:
    print(e)

# Deploy config set to CSR via Netmiko
changes = conn.send_config_set(configs)

# Write config changes to file
with open('changes.txt', 'w+') as f:
    f.write(changes)


# Get Startup config and write to a file
with open('startup.txt', 'w+') as f:
    f.write(conn.send_command('show start'))

with open('startup.txt', 'r') as f:
    data = f.read().splitlines(True)

with open('startup.txt', 'w') as f:
    f.writelines(data[4:])

# Get Running config and write to a file
with open('running.txt', 'w+') as f:
    f.write(conn.send_command('show run'))

with open('running.txt', 'r') as f:
    data = f.read().splitlines(True)

with open('running.txt', 'w') as f:
    f.writelines(data[6:])

# Open startup and running configs
f = open('startup.txt', 'r')
startup = f.readlines()
f.close()

f = open('running.txt', 'r')
running = f.readlines()
f.close()

# Compare and print differences using difflib Python library
for line in difflib.unified_diff(startup, running):
    print(line, end='')

