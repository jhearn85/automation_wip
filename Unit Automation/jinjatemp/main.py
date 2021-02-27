import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from datetime import datetime
import os.path
from unit_match import *
from unit_welcome import *
from getpass import getpass

# Create start time variable to view runtime
start_time = datetime.now()

# Initialize the jinja2 Environment to load templates
# from current directory

# Render the template and print the resulting document

# Output result to new template file for configuration export via Netmiko

# testing sys.argv - print(str(sys.argv))


if __name__ == "__main__":
    welcome_script()
    from unit_welcome import Device_Template

    user_unit()
    from unit_match import unit_ip

    template_configure(Device_Template, unit_ip)
