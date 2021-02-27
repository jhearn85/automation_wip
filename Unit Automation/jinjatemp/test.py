from user_credentials import User_Credentials
import ipaddress
import re
from datetime import datetime
import time
from getpass import getpass

User_Credentials()
from user_credentials import device


from sshconnect import sshconnect
sshconnect(device)
print(device)