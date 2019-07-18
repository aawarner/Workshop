'''
EXERCISE:

Given a netconf template called "exercise_template.xml" write a program that will
configure your CSR1000v interface GigabitEthernet2 with a description, ip address,
and subnet mask.

Hint!!!
Use the ncclient library to accomplish this.
'''

from device_info import csr
from ncclient import manager
import xml.dom.minidom

f = open("exercise_template.xml")
netconf_template = f.read()
f.close()


netconf_payload = netconf_template.format(int_name="GigabitEthernet2",
                                          int_desc="Configured by NETCONF",
                                          ip_address="11.12.13.14",
                                          subnet_mask="255.255.255.0")

print("Configuration Payload:")
print("-" * 30)
print(netconf_payload)


with manager.connect(
    host=csr["address"],
    port=csr["port"],
    username=csr["username"],
    password=csr["password"],
    hostkey_verify=False,
    ) as m:
    netconf_reply = m.edit_config(netconf_payload, target="running")
    print(xml.dom.minidom.parseString(str(netconf_reply)).toprettyxml())
