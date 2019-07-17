from device_info import csr
from ncclient import manager
import xmltodict
import xml.dom.minidom

f = open("filter.xml")
netconf_filter = f.read()
f.close()

with manager.connect(
    host=csr["address"],
    port=csr["port"],
    username=csr["username"],
    password=csr["password"],
    hostkey_verify=False,
) as m:
    netconf_reply = m.get(netconf_filter)
    route_details = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
    protocols = route_details["routing"]["routing-instance"][0]["routing-protocols"]

    print(xml.dom.minidom.parseString(str(netconf_reply)).toprettyxml())

    print("*" * 80)
    print("Current Routing Configuration:\n")
    print("Configured route types: " + protocols["routing-protocol"]["type"]["#text"])
    print("\nConfigured routes: ")
    print("Network   Nexthop\n")
    print(
        protocols["routing-protocol"]["static-routes"]["ipv4"]["route"]
        .get("destination-prefix")
        .get("#text")
        + " "
        + protocols["routing-protocol"]["static-routes"]["ipv4"]["route"]
        .get("next-hop")
        .get("next-hop-address")
    )
