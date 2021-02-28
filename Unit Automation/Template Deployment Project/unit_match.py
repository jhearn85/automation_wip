import time

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
    unit_codes = {
        "1MAR": "32",
        "1BN1MAR": "34",
        "2BN1MAR": "35",
        "3BN1MAR": "36",
        "1BN4MAR": "37",
        "5MAR": "38",
        "1BN5MAR": "40",
        "2BN5MAR" : "41",
        "3BN5MAR" : "42",
        "2BN4MAR" : "43",
        "7MAR": "44",
        "1BN7MAR": "46",
        "2BN7MAR" : "47",
        "3BN7MAR" : "48",
        "3BN4MAR" : "49",
        "11MAR": "62",
        "1BN11MAR": "64",
        "2BN11MAR" : "65",
        "3BN11MAR" : "66",
        "5BN11MAR" : "67",
        "1CEB" : "69",
        "1LAR" : "71",
        "3LAR" : "72",
        "1RECON" : "73",
        "CLR1" : "74",
        "CLB1" : "75",
        "CLB5" : "76",
        "CLB7" : "77",
        "MWCS38" : "78"
    }

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
    if verification != "y":
        print("Exiting Script, please try again")
        for i in range(3):
            print("!")
            time.sleep(0.5)
        quit()
    if Device_Template != "CS-template.j2":
        using_cs = input("Are you using a Core Switch in your Topology?: ")
        if using_cs == "y":
            switch_ports = input("\nWhat Device Ports will be connected to your switch? \nGive in standard format(as above) and seperated by comma(Eg: G0/0,G0/1,G0/2")
            #split user input and store as variables in port list
            replacement_dictionary["ports_to_cs"]=switch_ports.split(",")
        else:
            replacement_dictionary["external_port"] = input("\nWhat Device Port will be connected to your external fiber? \nGive in standard Format (G0/0, G0/1, etc)): ")
            replacement_dictionary["taclane_port"] = input("\nWhat Device Port will be connected to your Taclane? \nGive in standard Format (G0/0, G0/1, etc)): ")

    #Will have to implement if depending on device type - import from unit_welcome
    if Device_Template == "CS-template.j2":
        replacement_dictionary["ssh_port"] = input("\nWhat port is your device currently connected to for SSH access? Give in standard Format (G0/0, G0/1, etc): ")
        connection_types={"a" : "59", "b" : "101", "c" : "50"}
        external_connection = input("What Type of Device are you using for external Access?:\nA.Fiber(BAN)\nB.VSAT Large\nC.TAMPA\nPlease Give Answer in A/B/C Format: ").lower()
        replacement_dictionary["external_vlan"] = connection_types[external_connection]

        
        replacement_dictionary["external_port"] = input("\nWhat Device Port will be connected to your external connection? \nGive in standard Format (G0/0, G0/1, etc)): ")
        replacement_dictionary["taclane_port"] = input("\nWhat Device Port will be connected to your Taclane? \nGive in standard Format (G0/0, G0/1, etc)): ")
        replacement_dictionary["access_ports"] = input("Give a Range that will be used as access ports:\n Example: G0/10-20, or G025-45\n*************\nENSURE YOU DO NOT OVERWRITE IMPORTANT PORTS\n*************\nPort Range: ")
        #placeholder loopback to avoid erroring in template generation
        if replacement_dictionary["taclane_port"] == "":
            replacement_dictionary["taclane_port"]="Lo175"

        router_ports = input("\nWhat Device Ports will be connected to your router? \nGive in standard format(as above) and seperated by comma(Eg: G0/0,G0/1,G0/2")
        #split user input and store as variables in port list
        replacement_dictionary["ports_to_router"]=router_ports.split(",")

