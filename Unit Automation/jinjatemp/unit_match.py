import time


#takes user input and compares against dictionary of unit -> IP mappings
def user_unit():
    time.sleep(1)
    unit_code=''
    unit_codes = {
        '1MAR' : '32',
        '1BN1MAR' : '33',
        '5MAR' : '38',
        '1BN5MAR' : '39',
        '7MAR' : '44',
        '1BN7MAR' : '45',
        '11MAR' : '62',
        '1BN11MAR' : '63'
    }

    #retrieves user input and formats to match dict check - stores unit name and IP into variables
    while unit_code not in unit_codes:
        unit_code = input("Please enter your unit code (Please use -- xMARxBN -- format: ").upper()
        print("\n")
        if unit_code in unit_codes:
            unit_ip= unit_codes.get(unit_code)
        else:
            time.sleep(1)
            print("\n")
            print("**********************************************")
            print("Please enter a value in the specificed format!")
            print("**********************************************")
            print("\n")
            time.sleep(3)

    print("************************************\n")
    verification = input(f"Please verify you are in {unit_code}(Y/n): ").lower() 
    if verification != 'y':
        print("Exiting Script, please try again")


