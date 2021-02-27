from user_credentials import device
from netmiko import ConnectHandler
from netmiko.ssh_exception import (
    NetMikoAuthenticationException,
    NetMikoTimeoutException,
)

# def function to connect with netmiko framework defined per ip
def sshconnect(device):
cfg_file = "FinalTemplate.txt"
try:
    with ConnectHandler(**device) as conn:
        conn.send_config_from_file(cfg_file)
        conn.save_config()
        print(f"Configuration of device Successful")
except NetMikoAuthenticationException:
    print(f"Connection to Device {device['ip']} failed.")
except:
    print("what??")


