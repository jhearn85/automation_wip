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
        "a": "Fiber 3945 Router",
        "b": "Fiber 3850 Core Switch",
        "c": "VSAT 3945 Router",
    }
    # while loop to pull user input and define device type template
    while Device_Type not in ["a", "b", "c"]:
        print("*************************************************")
        Device_Type = input(
            f"What type of Device are you configuring?\nA - {devices['a']}\nB - {devices['b']}\nC - {devices['c']}\n\nPlease Select: "
        ).lower()
        if Device_Type == "a":
            Device_Template = "SPOKE-BC-NIPR-CISCO-3945_v3.4.j2"
        elif Device_Type == "b":
            Device_Template = "placeholder"
        elif Device_Type == "c":
            Device_Template = "placeholder"
        else:
            print("That is not a valid option, please try again.")
            time.sleep(2)

    time.sleep(1)
    print("\n*************************************************")
    verification = input(
        f"Please verify you are working on a {devices[Device_Type]}(Y/n): "
    ).lower()
    if verification != "y":
        print("Exiting Script, please try again")
        quit()
