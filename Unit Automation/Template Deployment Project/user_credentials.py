import ipaddress
import re
from datetime import datetime
import time
from getpass import getpass


def User_Credentials():
    global device
    time.sleep(2)
    ssh_reachable = input(
        "\n\nIs the Device to be Configured reachable via SSH on this computer(Y/n): "
    ).lower()
    if ssh_reachable != "y":
        print("\nPlease input these command on target device and retry this Wizard!")
        print("""\n 
hostname _______
username _______ priv 15 secret ________
ip domain-name usmc.mil
crypto key gen rsa label ssh-rsa modulus 2048
ip ssh version 2
ip ssh rsa key ssh-rsa
line vty 0 15
login local
        """)
        quit()
    device = {
        "ip": "temp",
        "username": "temp",
        "password": "temp",
        "device_type": "cisco_ios",
    }  # Temp device values for while validation loops

    # IP PULL
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"  # IP Regex check
    IP_Validity = False
    # while loop to check IP validity
    while not IP_Validity:
        device["ip"] = input("Please input a valid IP: ")
        IP_Validity = bool((re.search(regex, device["ip"])))
        if IP_Validity:
            print("Verifying IP...\n")
            time.sleep(1)
            print("IP Verified!\n")
        else:
            time.sleep(2)
            print(
                "\n*************************************************************************\nMalformed input! Please enter a valid IP and try again! (Eg: 192.168.0.1) \n*************************************************************************\n"
            )

    # USERNAME PULL
    device["username"] = input("What is the device's local username: ")
    un_verification = ""
    # Username verification loop
    while un_verification != "y":
        un_verification = input(
            f"Your username is {device['username']}, correct (Y/n)? "
        ).lower()
        if un_verification != "y":
            device["username"] = input("What is the device's local username: ")

    # PASSWORD PULL
    time.sleep(1)
    print(
        " \n ******************************************************************************* \n*Your Password will NOT be visible for security, ensure it is entered correctly!*\n ******************************************************************************* "
    )
    device["password"] = getpass()
