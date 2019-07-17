from device_info import csr
from ncclient import manager
import xml.dom.minidom

with manager.connect(host=csr["address"],
                     port=csr["port"],
                     username=csr["username"],
                     password=csr["password"],
                     hostkey_verify=False) as m:
    running = m.get_config("running")
    print(xml.dom.minidom.parseString(str(running)).toprettyxml())
