import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from datetime import datetime
import os.path
import time

def welcome_script():
    print("Welcome to the Unit Template Configuration Engine")
    time.sleep(2)
    Device_Type = ''
    while Device_Type not in ['a', 'b', 'c']: 
        Device_Type = input("What type of Device are you configuring?\nA - Fiber 3945 Router\nB - Fiber 3850 Core Switch\nC - VSAT 3945 Router\n Please Select: ").lower()
        if Device_Type == 'a':
            Device_Template = "SPOKE-BC-NIPR-CISCO-3945_v3.4.j2"
        elif Device_Type == 'b':
            Device_Template = "placeholder"
        elif Device_Type == 'c':
            Device_Template = "placeholder"
        else:
            print("That is not a valid option, please try again.")

user_unit_name=input("What is your unit name: ")

unit_info = {'third_octet' : user_unit_name}
#Create start time variable to view runtime
start_time = datetime.now()
jinjadir =  './jinjatemp'
#Initialize the jinja2 Environment to load templates
#from current directory
x = None

while x != '1' and x != '2':
    x = input("Please input a number 1 or 2: ")
    if x == '1':
        print('1')
    elif x == '2':
        print ('2')
    else:
        print ('Neither 1 nor 2.')

print ("all OK")


def template_loader(template_file)
env = Environment(loader=FileSystemLoader(jinjadir))
template = env.get_template(template_file)

#Render the template and print the resulting document
rendered_template = template.render(**unit_info)
print(rendered_template)

#Output result to new template file for configuration export via Netmiko
with open("FinalTemplate.txt", "w") as New_Template:
    New_Template.write(rendered_template)
    New_Template.close
# testing sys.argv - print(str(sys.argv))
