
import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from datetime import datetime
import os.path



def user_input():
    description = input("Give a Description: ")
    IP_Address = input("Give your IP: ")
    user_input.desc = description
    user_input.ip = IP_Address

user_input()

Description = user_input.desc
IP_Address = user_input.ip
with open('data.yaml', 'w') as outfile:
    outfile.write(yaml.dump(
        {"Interfaces": {
        'Description' : Description,
        'ip' : IP_Address}
        },
    default_flow_style=False))
