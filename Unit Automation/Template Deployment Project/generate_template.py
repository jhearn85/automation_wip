import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from datetime import datetime
import time
import os.path


def fiber_template_configure(templatetype, replacement_dictionary):
    file_loader = FileSystemLoader(".")
    env = Environment(loader=file_loader)
    template = env.get_template(templatetype)
    output = template.render(**replacement_dictionary)

    with open("FinalTemplate.txt", "w") as New_Template:
        New_Template.write(output)
        New_Template.close()
    print("\n**********************************")
    print("Creating Template, please standby.")
    for i in range(5):
        time.sleep(0.5)
        print(".")
    print("Template Created Successfully, file saved as 'FinalTemplate.txt'")
