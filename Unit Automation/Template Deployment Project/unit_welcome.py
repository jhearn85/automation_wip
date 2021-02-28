import time


# Registers users input and defines the template to use for jinja2 -> final device template

Device_Template = ""


def welcome_script():
    global Device_Template
    print("*************************************************")
    print("Welcome to the Unit Template Configuration Engine")
    print("*************************************************")
    time.sleep(2)

    # empty str to hold None user device type before running while loop
    Device_Type = ""
    devices = {
        "a": "Fiber - Cisco 3945 Router",
        "b": "VSAT - Cisco 3945 Router",
        "c": "Cisco 3850 Core Switch",
        "d": "NOTM "

    }
    # while loop to pull user input and define device type template
    while Device_Type not in ["a", "b", "c"]:
        print("*************************************************")
        Device_Type = input(
            f"What type of Device are you configuring?\nA - {devices['a']}\nB - {devices['b']}\n\nPlease Select: "
        ).lower()

        #Checks to see if CS is being implemented
        using_cs = input(
            "\nWill your topology include a Core Switch? (Router -> CS -> Fiber/VSAT/Taclane/etc)\n ***SELECT NO IF CS ALREADY CONFIGURED*** [Y/n]: "
        ).lower()

        #Sets Device Template to Core Switch if still has to be configured
        if using_cs == "y":
            print("We will be configuring your Core Switch First! Please ensure this device is connected to it and accessible via SSH.")
            Device_Type = "c"
        
        #Selects Device Template for J2 conversion
        if Device_Type == "a":
            Device_Template = "SPOKE-BC-NIPR-CISCO-3945_v3.4.j2"
        elif Device_Type == "b":
            Device_Template = "SPOKE-BC-NIPR-CISCO-VSAT-3945.j2"
        elif Device_Type == "c":
            Device_Template = "CS-template.j2"
        else:
            print("That is not a valid option, please try again.")
            time.sleep(2)
    print(Device_Template)
    time.sleep(1)
    print("\n*************************************************")
    verification = input(
        f"Please verify you are working on a {devices[Device_Type]}(Y/n): "
    ).lower()
    if verification != "y":
        print("Exiting Script, please try again")
        quit()
