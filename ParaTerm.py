# SSH Client for iOS Devices **ONLY** (currently)
"""
Supported Devices:
	( ON DEVICE )
*	iPhone (All devices / versions (Latest, 13.3))
* 	iPad (All devices with latest jailbreak)
*	iPod (Alld devices with jailbreak)

	Requirements:
		( ON DEVICE )
	*	OpenSSH (via Cydia) - Get it here: https://cydia.saurik.com/openssh.html
	* 	A jailbroken iOS Device

Supported Devices:
	( ON COMPUTER )
* Windows
* Mac OS
* Linux
	( virtually any machine that can run Python. )

Requirements:
	( ON COMPUTER )
* Python 3.6.0 (3.6 is the latest version you can use, anything above will give you a failed pip setup)
[!] Install ssh2-python using pip (pip(3) install ssh2-python)

CHANGELOG:

* Initial Release - 13/03/2020
* Added SSH2 environment

NOTES:

* This is the first initial release, please don't expect this program to work without flaws.
* Commands can only be used one at a time (no loop is included yet, if you have the time, please feel free to push this Git and i'll add it.)
	
"""

import socket
from ssh2.session import Session
import getpass

# variables
ios = input("Are you targetting an iOS device? ")
run = input("Are you running LOCALLY? ")
uname = getpass.getuser()

if "y" in ios:
	print("Setting environment to target iOS devices...\n")
	pass
elif "n" in ios:
	print("Cannot change environment in BETA version, check back later\nExiting...")
	exit()
elif "y" in run:
	print('Setting environment to LOCAL\n')
elif "n" in run:
	print("Cannot change environment in BETA version, check back later\nExiting...")
	exit()


# print ios hostnames
print("---------+ iOS Device info ---------+\nUsername: root\nPassword: alpine\n---------+ END ---------+\n")

# find host (ip)
host = input("[!] Enter Devices WiFi IP Address: ")
# find root username
user = input("[!] Enter hostname (eg. root): ")
# find password
passwd = input("[!] Enter host password (eg. alpine): ")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, 22))

# open an SSH session
session = Session()

# socket handshake
session.handshake(sock)

# make a connection with our Username and Password
session.userauth_password(user, passwd)

# define channel

channel = session.open_session()

# get cmds
test_cmd = input("[+] Please input a test command >> ")
channel.execute(test_cmd)
size, data = channel.read()
while size > 0:
	print(data.decode())
	size, data = channel.read()
channel.close()

# define exit status
print("Exit Status: {0}".format(channel.get_exit_status()))

# todo:
# +---+
# Add a command while loop so more commands can be executed