import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from datetime import datetime
import os.path
from unit_match import *
from unit_welcome import *
from netmiko import ConnectHandler
from netmiko.ssh_exception import (
    NetMikoAuthenticationException,
    NetMikoTimeoutException,
)


def main(templatetype, ip):
    file_loader = FileSystemLoader('.')
    env = Environment(loader=file_loader)
    template = env.get_template(templatetype)
    output = template.render(third_octet=ip)

    with open("FinalTemplate.txt", "w") as New_Template:
        New_Template.write(output)
        New_Template.close()

#Create start time variable to view runtime
start_time = datetime.now()

#Initialize the jinja2 Environment to load templates
#from current directory

#Render the template and print the resulting document

#Output result to new template file for configuration export via Netmiko

# testing sys.argv - print(str(sys.argv))




# def function to connect with netmiko framework defined per ip
def send_cmd(device):
    cfg_file = "FinalTemplate.txt"
    try:
        with ConnectHandler(**device) as conn:
            conn.send_config_from_file(cfg_file)
            conn.save_config()
            print(f"Configuration of device Successful")
    except NetMikoAuthenticationException:
        print(f"Connection to Device {device['ip']} failed.")
    except:
        pass



def devices():
        device = {
            "ip": user_ip_address,
            "username": user_username,
            "password": user_password,
        }



if __name__ == "__main__":
    welcome_script()
    from unit_welcome import Device_Template
    user_unit()
    from unit_match import unit_ip
    main(Device_Template, unit_ip)
    print("\n")
    print("**********************************")
    print("Creating Template, please standby.")
    for i in range(5):
        time.sleep(.5)
        print(".")
    print("Template Created Successfully, file saved as 'FinalTemplate.txt'")
    print("\n\n")
    time.sleep(2)
    ssh_reachable=input("Is the Device to be Configured reachable via SSH on this computer(Y/n): ").lower()
    if ssh_reachable != "y":
        print("Please do xxxxxxx to configure SSH and retry this Wizard!")
        exit
    