import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from datetime import datetime
import os.path

#Create start time variable to view runtime
start_time = datetime.now()
jinjadir =  '.\jinjatemp'
#Initialize the jinja2 Environment to load templates
#from current directory
env = Environment(loader=FileSystemLoader(jinjadir))
template = env.get_template(sys.argv[1])


file = "\YAML\data.yaml"
path = os.getcwd()+file
#Load the context YAML file into a python dictionary (context)
with open(path, 'r') as datafile:
    context = yaml.load(datafile, Loader = yaml.FullLoader)

#Render the template and print the resulting document
rendered_template = template.render(**context)
print(rendered_template)

#Output result to new template file for configuration export via Netmiko
with open("FinalTemplate.py", "w") as New_Template:
    New_Template.write(rendered_template)
    New_Template.close
# testing sys.argv - print(str(sys.argv))





#Utilizing Template to auto-configure IOS via netmiko
#Define routers and build dictionary
R1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.17',
    'username': 'admin',
    'password': 'password',
}
R2 = {
    'device_type': 'cisco_ios',
    'host': '192.168.0.18',
    'username': 'admin',
    'password': 'password',
}
all_routers = [R2]


#Loop through routers commiting template - currently only works when configuring single router
#Will reintroduce R2 when that is resolved
for a_router in all_routers:
    net_connect = ConnectHandler(**a_router)
    #For some reason this is failing if I put it as a .txt file, using .py for now
    output = net_connect.send_config_from_file(config_file = 'FinalTemplate.py')
    #print(f"\n\n---------- Device {a_router['device_type']} {a_router['host']}----------")
    print(output)
    #print("------ End -------")

end_time = datetime.now()
total_time = end_time - start_time
print(total_time)


























##################################################################################################
#py render_template.py template.jinja2 data.yaml > TestTemplate.txt
# ^^^^Creates Template using the .jinja2 template and .yaml context - outputs to TestTemplate.txt^^^^
##################################################################################################
