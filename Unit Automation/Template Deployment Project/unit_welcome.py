import time
import shutil

# Registers users input and defines the template to use for jinja2 -> final device template

Device_Template = ""


def welcome_script():
    def wrong_input():
        time.sleep(1)
        print("\n**********************************************\nThat is not a valid option, please try again.\n**********************************************\n")
        time.sleep(2)
    global Device_Template
    print("*************************************************")
    print("Welcome to the Unit Template Configuration Engine")
    print("Please ensure all physical cabling is complete,\nWe will be referencing these connections in the future!")
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
        if Device_Type in ["a", "b", "c"]:
            
            
            #Checks to see if CS is being implemented
            using_cs =''
            while using_cs not in ['y', 'n']:
                using_cs = input(
                    "\n\nWill your topology include a Core Switch? (Router -> CS -> Fiber/VSAT/Taclane/etc)\n\n***SELECT NO IF CS ALREADY CONFIGURED***[Y/n]: "
                ).lower()
                if using_cs == "n":
                    continue
                    #Sets Device Template to Core Switch if still has to be configured
                elif using_cs == "y":
                    print("\nWe will be configuring your Core Switch First! \nPlease ensure this device is connected to it and accessible via SSH.")
                    Device_Type = "c"
                else:
                    wrong_input()
        
        #Selects Device Template for J2 conversion
        if Device_Type == "a":
            Device_Template = "SPOKE-BC-NIPR-CISCO-3945_v3.4.j2"
        elif Device_Type == "b":
            Device_Template = "SPOKE-BC-NIPR-CISCO-VSAT-3945.j2"
        elif Device_Type == "c":
            Device_Template = "CS-template.j2"
        else:
            wrong_input()
    print(Device_Template)
    time.sleep(1)
    print("\n**************************************************************")
    verification = input(
        f"Please verify you are working on a {devices[Device_Type]}(Y/n): "
    ).lower()
    if verification != "y":
        for _ in range(3):
            time.sleep(0.3)
            print(".")
        print("Exiting Script, please try again")
        quit()
    else:
        shutil.copy(f"/var/NetAuto/Unit Automation/Template Deployment Project/device_templates/{Device_Template}", "/var/NetAuto/Unit Automation/Template Deployment Project" )

