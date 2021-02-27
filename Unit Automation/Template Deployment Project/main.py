import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from datetime import datetime
import os.path
from unit_match import *
from unit_welcome import *
from generate_template import template_configure
from user_credentials import User_Credentials
from sshconnect import sshconnect
from getpass import getpass

# Create start time variable to view runtime
start_time = datetime.now()


if __name__ == "__main__":
    welcome_script()
    from unit_welcome import Device_Template
    user_unit()
    from unit_match import unit_ip
    template_configure(Device_Template, unit_ip)
    User_Credentials()
    from user_credentials import device
    sshconnect(device)
    end_time = datetime.now()
    total = end_time - start_time
    print(f"\nScript time to completion: {total}")