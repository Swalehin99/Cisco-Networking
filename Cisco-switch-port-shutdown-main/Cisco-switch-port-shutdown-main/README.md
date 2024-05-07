# Cisco-switch-port-shutdown
This Python script allows you to automate the shutdown of ports on Cisco switches. You can specify the switch IPs and the ports to be shut down in separate text files.
#Prerequisites
Python 3.
Netmiko library (pip install netmiko)
UsageClone the repository:git 
clone https://github.com/ACCIEDevNet/Cisco-switch-port-shutdown.git
Install the required dependencies:
pip install netmiko
Prepare your input files:switch_ips.txt: 
List the IP addresses of the switches, one per line.
Example:
192.168.1.1
192.168.1.2
switch_ports.txt: Specify the ports to be shut down for each switch in the format switch_ip:port1,port2. 
Separate multiple ports with commas.Example:
192.168.1.1:Gi0/1,Gi0/2
192.168.1.2:Gi0/3,Gi0/4
Run the script:python shutdown_ports.py
Follow the prompts and enter your credentials if required.
NotesMake sure your Cisco switches are accessible via SSH.
Update the script with your actual username and password.
Ensure that the specified ports exist on the switches.
