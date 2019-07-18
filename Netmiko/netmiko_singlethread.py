import netmiko
from datetime import datetime
import sys

f = open("devices.txt", "r")
devices = f.read()
devices = devices.strip().splitlines()
f.close()


start_time = datetime.now()

for device in devices:
    try:
        connection = netmiko.ConnectHandler(
            ip=device, device_type="cisco_ios", username="cisco", password="cisco", timeout=10
        )
        print("#" * 80)
        print(connection.send_command("show Run"))
        print("#" * 80)
        connection.disconnect()
    except (netmiko.NetMikoTimeoutException, netmiko.NetMikoAuthenticationException,) as e:
        print(e)
        sys.exit()


print("\nElapsed time: " + str(datetime.now() - start_time))
print("Configuration collection finished")


