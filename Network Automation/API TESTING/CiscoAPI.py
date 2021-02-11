
import requests
import json
from pprint import pprint
import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
from datetime import datetime
import os.path


#ATTEMPT AT INTEGRATING TEMPLATE BUILDER WITH RESTAPI
JSON_TEMPLATES = Environment(loader=FileSystemLoader('.'), trim_blocks=True)
url = "https://192.168.0.111/"

def get_token(username, password):
    partial_url = "api/aaaLogin.json"
    template = JSON_TEMPLATES.get_template("login.j2.json")
    payload = template.render(username=username, password=password)
    new_url=url+partial_url
    requests.packages.urllib3.disable_warnings()
    response = requests.post(new_url, data=payload, verify=False).json()
    token = response['imdata'][0]['aaaLogin']['attributes']['token']
    print(token)
    return token
def main():
    token = get_token("admin", "password")
if __name__ == "__main__":
    main()



#TESTING\/\/
import requests
import json

def get_token():  
   url = "https://192.168.0.100/api/aaaLogin.json"

   payload = {
      "aaaUser": {
         "attributes": {
            "name":"admin",
            "pwd":"---"
         }
      }
   }

   headers = {
      "Content-Type" : "application/json"
   }

   requests.packages.urllib3.disable_warnings()
   response = requests.post(url,data=json.dumps(payload), headers=headers, verify=False).json()

   token = response['imdata'][0]['aaaLogin']['attributes']['token']
   return token

def main():
   token = get_token()
   print("The token is: " + token)

if __name__ == "__main__":
   main()


#TESTING^^^










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
   "port": "443",
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
      print(f"{interface['name']} -- {interface['description']} -- {interface['ietf-ip:ipv4']['address'][0]['ip']}")


















#THIS IS VIA THE CSR_MGMT RESTFULAPI - Cisco Proprietary via iosxe OVA

import requests
import urllib3
import json

ip_address = '192.168.0.111'
interface = 'GigabitEthernet1'
username = 'admin'
password = 'password'

def get_token():
    """
    Authenticate and get token
    """

    url = 'https://%s:55443/api/v1/auth/token-services' % ip_address
    auth = (username, password) 
    headers = {'Content-Type':'application/json'}
    response = requests.post(url, auth=auth, headers=headers, verify=False)
    json_data = json.loads(response.text)
    token = json_data['token-id']
    print('We received token: %s' % token)
    return token    
    print(response.text)


def get_interface(token, interface):
    """
    Retrieve interface information from router.
    """
    
    url = 'https://%s:55443/api/v1/interfaces/%s' % (ip_address, interface)
    headers={ 'Content-Type': 'application/json', 'X-auth-token': token}

    response = requests.get(url, headers=headers, verify=False)
    json_data = json.loads(response.text)
    print("Here is the interface information: \n")
    print(json.dumps(json_data, indent=4, separators=(',', ': ')))


def put_interface(token, interface):
    """
    Retrieve interface information from router.
    """
    url = 'https://%s:55443/api/v1/interfaces/%s' % (ip_address, interface)
    headers={ 'Content-Type': 'application/json', 'X-auth-token': token}

    payload = {
        'type':'ethernet',
        'if-name':interface,
        'ip-address':'11.11.11.11',
        'subnet-mask':'255.255.255.255',
        'description': 'TEST-PUT-INTERFACE'
        }

    response = requests.put(url, headers=headers, json=payload, verify=False)
    print('The router responds with status code: %s ' % response.status_code)


# Disable unverified HTTPS request warnings.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get token.
token = get_token()



# GET interface information.
get_interface(token, interface)

# PUT interface information.
put_interface(token, interface)
