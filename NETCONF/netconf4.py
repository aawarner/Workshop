from device_info import csr
from ncclient import manager
import xmltodict



with manager.connect(
    host=csr["address"],
    port=csr["port"],
    username=csr["username"],
    password=csr["password"],
    hostkey_verify=False,
) as m:
    netconf_reply = m.get(filter=("xpath",
                                  "/routing/routing-instance/routing-protocols"))


    route_details = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
    protocols = route_details["routing"]["routing-instance"][1]["routing-protocols"]

    print("*" * 80)
    print("Current Routing Configuration:\n")
    print("Configured route types: " + protocols["routing-protocol"]["type"])
    print("\nConfigured routes: ")
    print("Network   Nexthop\n")
    print(
        protocols["routing-protocol"]["static-routes"]["ipv4"]["route"]
        .get("destination-prefix")
        + " "
        + protocols["routing-protocol"]["static-routes"]["ipv4"]["route"]
        .get("next-hop")
        .get("next-hop-address")
    )