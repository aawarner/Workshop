from device_info import csr
from ncclient import manager

m = manager.connect(host=csr["address"],
                     port=csr["port"],
                     username=csr["username"],
                     password=csr["password"],
                     hostkey_verify=False)
for i in m.server_capabilities:
    print(i)

m.close_session()
