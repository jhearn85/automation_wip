from user_credentials import User_Credentials
from datetime import datetime
import time
from netmiko import ConnectHandler
from netmiko.ssh_exception import (
    NetMikoAuthenticationException,
    NetMikoTimeoutException,
)

# function that generates device dict must be run first!!!
# def function to connect with netmiko framework defined per ip
def sshconnect(device):
    cfg_file = "FinalTemplate.txt"
    try:
        with ConnectHandler(**device) as conn:
            print("Attempting configuration transfer - Please be patient")
            conn.send_config_from_file(cfg_file, delay_factor=5)
            conn.save_config()
            for i in range(5):
                time.sleep(0.5)
                print(".")
            print("!")
            print(f"Configuration of device Successful")
    except NetMikoAuthenticationException:
        print(f"Connection to Device {device['ip']} failed.")
    except NetMikoTimeoutException:
        print("\n")
        print("        *********************************")
        print("        *            ERROR              *")
        print("        *********************************")
        print("Device Timeout - Please valid SSH connectivity and try again! ")
