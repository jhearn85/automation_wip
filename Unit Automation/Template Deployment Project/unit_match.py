import time
from value_check import regex_check
from unit_codes import unit_codes
import os.path
from os import path


# takes user input and compares against dictionary of unit -> IP mappings
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

def user_unit():
    from unit_welcome import Device_Template
    global replacement_dictionary
    time.sleep(1)
    unit_code = ""

    verification =''
    while verification != 'y':
        # retrieves user input and formats to match dict check - stores unit name and IP into variables
        while unit_code not in unit_codes:
            unit_code = input(
                "Please enter your unit code (Please use -- xMARxBN -- format (1BN5MAR - CLB1 - 1RECON)): "
            ).upper()
            print("\n")
            if unit_code in unit_codes:
                replacement_dictionary["unit_ip"] = unit_codes.get(unit_code)
            else:
                time.sleep(1)
                print("\n**********************************************")
                print("Please enter a value in the specificed format!")
                print("**********************************************\n")
                time.sleep(3)
        print("************************************\n")
        verification = input(
            f"Please verify you are in {unit_code}(Y/n): "
        ).lower()
        unit_code=""

    
    time.sleep(3)
    print("\n*******************************************************\nWe Will now be taking your device connection details!\nPlease verify with your physical topology!\n*******************************************************\n")
    #Jinja values if configuring device that is not Core Switch
    if path.exists("SPOKE-BC-NIPR-CISCO-3945_v3.4.j2") or path.exists("SPOKE-BC-NIPR-CISCO-VSAT-3945.j2"):
        if path.exists("CS-template.j2"):
                switch_ports = input("\nWhat Device Ports will be connected to your switch? \nGive in standard format(as above) and seperated by comma(Eg: G0/0,G0/1,G0/2): ")
                #Port name verification and store into dictionary list
                regex_check(switch_ports, replacement_dictionary, "ports_to_cs")

            #Values if using Direct Links to external devices (NON-Core Switch Topology)    
        else:
            external_port = input("\nWhat Device Port will be connected to your external fiber? \nGive in standard Format (G0/0, G0/1, etc)): ")
            regex_check(external_port, replacement_dictionary, "external_port")
            
            taclane_port = input("\nWhat Device Port will be connected to your Taclane? \nGive in standard Format (G0/0, G0/1, etc)): ")
            regex_check(taclane_port, replacement_dictionary, "taclane_port")



    #Gathering Values for Core Switch Jinja2 Template
    else:
        
        #while loop to verify input matches vlan options
        external_connection=""
        connection_types={
            "a" : "59",
            "b" : "101",
            "c" : "50"
        }

        while external_connection not in ["a", "b", "c"]:
            external_connection = input("What Type of Device are you using for external Access?:\nA.Fiber(BAN)\nB.VSAT Large\nC.TAMPA\nPlease Give Answer in A/B/C Format: ").lower()
            if external_connection in connection_types:
                replacement_dictionary["external_vlan"] = connection_types[external_connection]
                time.sleep(2)
            else:
                for i in range(3):
                    print(".")
                    time.sleep(0.5)
                print("X")
                print("Please enter a valid input!\n")
    

        ssh_port = input("\nWhat port is your device currently connected to for SSH access? Give in standard Format (G0/0, G0/1, etc): ")
        regex_check(ssh_port, replacement_dictionary, "ssh_port")

        external_port=input("\nWhat Device Port will be connected to your external connection? \nGive in standard Format (G0/0, G0/1, etc)): ")
        regex_check(external_port, replacement_dictionary, "external_port")

        taclane_port = input("\nWhat Device Port will be connected to your Taclane? \n Give placeholder port if no Taclane\nGive in standard Format (G0/0, G0/1, etc)): ")
        regex_check(taclane_port, replacement_dictionary, "taclane_port") 
        
        #Need to make regex check to verify string output correct
        replacement_dictionary["access_ports"] = input("Give a Range that will be used as access ports:\n Example: G0/10-20, or G025-45\n*************\nENSURE YOU DO NOT OVERWRITE IMPORTANT PORTS\n*************\nPort Range: ")
        

        router_ports = input("\nWhat Device Ports will be connected to your router? \nGive in standard format(as above) and seperated by comma(Eg: G0/0,G0/1,G0/2): ")
        regex_check(router_ports, replacement_dictionary, "ports_to_router")
        print(replacement_dictionary)