from netmiko import ConnectHandler
import time


# Function to read IPs from a file
def read_ips(filename):
    with open(filename, 'r') as file:
        ips = [line.strip() for line in file.readlines() if line.strip()]
    return ips


# Function to read port details from a file
def read_ports(filename):
    ports = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                switch_ip, port_list = line.strip().split(':')
                ports[switch_ip] = port_list.split(',')

    return ports


# Read switch IPs from a file
switch_ips = read_ips('switch_ips.txt')
print(switch_ips)
# Read port details from a file
switch_ports = read_ports('switch_ports.txt')
print(switch_ports)
time.sleep(3)


# Function to shut down ports on a switch
def shutdown_ports(switch_ip, ports):
    try:
        device = {
            'device_type': 'cisco_ios',
            'ip': switch_ip,
            'username': 'admin',  # Update with your username
            'password': "password",  # Update with your password
        }

        connection = ConnectHandler(**device)
        output = ''
        for port in ports:
            commands = [f'interface {port}',
                        'no shutdown']
            output += connection.send_config_set(commands)
            output += connection.send_command('write memory')  # Save configuration
            print(output)
        connection.disconnect()
        return output
    except Exception as e:
        return f"Error: {e}"


# Main loop to iterate over switches and shut down ports
for switch_ip in switch_ips:
    if switch_ip in switch_ports:
        ports = switch_ports[switch_ip]
        result = shutdown_ports(switch_ip, ports)
        print(f"Switch {switch_ip}: {result}")
    else:
        print(f"No ports to shut down on switch {switch_ip}")