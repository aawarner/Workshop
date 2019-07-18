import netmiko as n

f = open("devices.txt", "r")
devices = f.read()
devices = devices.strip().splitlines()
f.close()

config = ["router ospf 1", "network 11.10.10.0 255.255.255.0 area 0", "passive-interface default"]

for device in devices:
    try:
        connection = n.ConnectHandler(
            ip=device, device_type="cisco_ios", username="cisco", password="cisco"
        )
        connection.send_config_set(config)
        print(connection.send_command("show run | beg router ospf"))
        connection.disconnect()
    except (n.NetMikoTimeoutException, n.NetMikoAuthenticationException,) as e:
        print(e)
