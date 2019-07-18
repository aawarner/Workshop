import threading
from datetime import datetime
import netmiko
import getpass

f = open("devices.txt", "r")
devices = f.read()
devices = devices.strip().splitlines()
f.close()

user = input("Enter SSH login username: ")
pwd = getpass.getpass("Enter SSH login password: ")

def command(device):
    """Execute show run command using Netmiko."""
    try:
        connection = netmiko.ConnectHandler(ip=device, device_type="cisco_ios", username=user, password=pwd)
        print()
        print("#" * 80)
        print(connection.send_command_expect("show run"))
        print("#" * 80)
        print()
        connection.disconnect()
    except (netmiko.NetMikoTimeoutException, netmiko.NetMikoAuthenticationException,) as e:
        print(e)


def main():
    """
    Use threads and Netmiko to connect to each of the devices. Execute
    'show run' on each device. Record the amount of time required to do this.
    """
    start_time = datetime.now()

    for device in devices:
        thread = threading.Thread(target=command, args=(device,))
        thread.start()


    main_thread = threading.currentThread()

    for threads in threading.enumerate():
        if threads != main_thread:
            print(threads)
            threads.join()

    print("\nElapsed time: " + str(datetime.now() - start_time))


if __name__ == "__main__":
    main()