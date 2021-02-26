
#THIS IS VIA THE RESTCONF - STANDARD COMPATIBLE via RESTCONF CLI CMD
from getpass import getpass
import requests
import json
from pprint import pprint
import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from datetime import datetime
import os.path

device = {
   "ip": input("Please Give me your IP: "),
   "username": input("Please Give me your Username: "),
   "password": getpass(),
   "port": 443,
}

headers = {
      "Accept" : "application/yang-data+json", 
      "Content-Type" : "application/yang-data+json", 
   }

module = "ietf-interfaces:interfaces"

url = f"https://{device['ip']}:{device['port']}/restconf/data/{module}"


payload = {
   "interface": [
    {
      "name": "Loopback10000",
      "description": "Adding loopback10000",
      "type": "iana-if-type:softwareLoopback",
      "enabled": "true",
      "ietf-ip:ipv4": {
        "address": [
          {
            "ip": "192.0.2.60",
            "netmask": "255.255.255.255"
          }
        ]
      }
    }
  ]
 }

requests.packages.urllib3.disable_warnings()
response = requests.post(url, headers=headers, data=json.dumps(payload), auth=(device['username'], device['password']), verify = False)

if (response.status_code == 201):
   print("Successfully added interface")
else:
   print("Issue with adding interface")
    


response = requests.get(url, headers=headers, auth=(device['username'], device['password']), verify=False).json()


interfaces = response['ietf-interfaces:interfaces']['interface']

for interface in interfaces:
    if bool(interface['ietf-ip:ipv4']): #check if IP address is available
        #using .get() for interface provides protection from KeyError
      print(f"{interface['name']} -- {interface.get('description')} -- {interface['ietf-ip:ipv4']['address'][0]['ip']}")
















