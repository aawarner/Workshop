from device_info import csr
from ncclient import manager

f = open("template.xml")
netconf_template = f.read()
f.close()


netconf_payload = netconf_template.format(ip_address="202.100.100.0/24", next_hop_ip="10.10.10.1")

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

    print(netconf_reply)
