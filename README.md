# comp116_final_project
Jacob Ehrlich
December 12th, 2018
firetv.py

1. Acknowledgements

Inspiration for this project came from reading this article: 

https://hackaday.com/2018/04/18/fix-your-insecure-amazon-fire-tv-stick/

I'm using the nmap-python library to perform the port scans.

2. Usage

This python program requires an internet connection, arp-scan installed, and
adb installed. The script will run commands using arp-scan and adb and thus
will cause an error if those names are not found. nmap-python is also a
required library and should be in the local directory along with this program.

Usage is really simple. Run with:

$ python3 firetv.py

3. Features

The program will output each port scan on all the IP addresses on a network,
but will only check for port 5555. Once the output finds a device with port
5555 open, it will attempt to connect to it with adb. If the port scan and
connection are successful, the program will run a sequence of remote commands
that will (almost) hard reset the connected firestick. For demonstration
purposes, the program navigates to the hard reset option but DOES NOT hit
enter.

4. Limitations

The program relies on adb debugging turned on for the firestick device being
attacked. Otherwise, all the port scans will return closed and the program
will exit. Furthermore, there is also reliance on the user of the firestick
accepting your request to connect (if it's a more recent version) and thus
the script may have to be run a second time once the user agrees to add
your computer as a known device.

5. Purpose

The real point of this program is to demonstrate how easy it is to connect to
insecure IoT devices. While there are several dependencies, many people don't
know what adb debugging even is and whether it should be on or off. Similarly
Amazon has recently added a protective feature that displays a warning to
the user of their FireStick should a computer try and connect. You'd be 
surprised, however, at how many people just blindly hit ok and let my script
do its thing.
