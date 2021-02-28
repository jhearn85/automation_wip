import re
import time

def regex_check(import_value, dictionary, dictionary_slot):
    regex="^(Gig|gig|Gi|gi|g|F|f|Fa|fa)\d+[/]?[\d+]?[/]?[\d+]?[\.]?[\d+]?[/]?[\d+]?[/]?[\d+]?[:]?[\d+]?$"
    valid=False
    while valid==False:
        try:
            #Attempt Splitting if more than one port
            ports = import_value.split(",")
            for port in ports:
                valid=bool((re.search(regex, port)))
                if valid:
                    print("Verifying port...\n")
                    time.sleep(1)
                    print("Port Verified!\n")
                    dictionary[dictionary_slot] = ports
                else:
                    print("That is not a valid input! Please input a value in the format specified.")
                    import_value =input("give me a valid input in the specified format: ")
        except:
            #Check port value, if wrong retry import_value
            valid=bool((re.search(regex, import_value)))
            if valid:
                print("Verifying port...\n")
                time.sleep(1)
                print("Port Verified!\n")
                dictionary[dictionary_slot] = import_value
            else:
                print("That is not a valid input! Please input a value in the format specified.")
                import_value =input("give me a valid input in the specified format: ")
