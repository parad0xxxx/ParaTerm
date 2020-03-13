# ParaTerm
A python-based SSH client for jailbroken iOS devices.

#### What it does?
* In the simplest form possible, we emulate Terminal / SSH Linux on cross-platform devices
* We run our client _locally_, meaning we don't support port-forwarding.


#### Requirements:
* A jailbroken iDevice with OpenSSH installed.
    * [!] Get it here if you don't already have it: https://cydia.saurik.com/openssh.html
    
* A computer connected to the same network
* Python 3.6.0 with ssh2-python installed
    * [!] Get it here if you don't already have it: https://www.python.org/downloads/release/python-360/
    * ```pip install ssh2-python```
    
#### Output / Results:
```
Are you targetting an iOS device? yes
Are you running LOCALLY? yes
Setting environment to target iOS devices...

---------+ iOS Device info ---------+
Username: root
Password: alpine
---------+ END ---------+

[!] Enter Devices WiFi IP Address: 192.168.0.6
[!] Enter hostname (eg. root): root
[!] Enter host password (eg. alpine): alpine
[+] Please input a test command >> id
uid=0(root) gid=0(nobody) groups=0(nobody),1(daemon),2(kmem),3(sys),4(tty),5(operator),8(procview),9(procmod),20(staff),29(certusers),80(admin)

Exit Status: 0
```
