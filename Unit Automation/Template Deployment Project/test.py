import re
import time
from value_check import regex_check

replacement_dictionary = {
    "unit_ip" : "",
    "ssh_port" : "",
    "external_vlan" : "",
    "external_port" : "",
    "taclane_port" : "",
    "ports_to_router" : [],
    "ports_to_cs" : [],
    "access_ports" : ""
    
}

external_port = input("\nWhat Device Port will be connected to your external fiber? \nGive in standard Format (G0/0, G0/1, etc)): ")

regex_check(external_port, replacement_dictionary, "external_port")
print(replacement_dictionary["external_port"])
print("test")






class topology:
    def __init__(self, devices, connections):
        self.devices = devices
        self.connections = connections
    def topfunc(self):
        print("test")

top = topology("router", "")