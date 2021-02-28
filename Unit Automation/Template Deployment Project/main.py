import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from datetime import datetime
import os.path
from unit_match import *
from unit_welcome import *
from generate_template import fiber_template_configure
from user_credentials import User_Credentials
from sshconnect import sshconnect
from getpass import getpass
import time
# Create start time variable to view runtime
start_time = datetime.now()


if __name__ == "__main__":
    welcome_script()
    from unit_welcome import Device_Template
    print(Device_Template + "in main")
    user_unit()
    #Based on Fiber
    from unit_match import replacement_dictionary
    print(replacement_dictionary)
    fiber_template_configure(Device_Template, replacement_dictionary)
    User_Credentials()
    from user_credentials import device
    sshconnect(device)
    end_time = datetime.now()
    total = end_time - start_time
    print(f"\nScript time to completion: {total}")