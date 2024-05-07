import paramiko
import time
from _datetime import datetime

def cisco_switch_login(ip_address, username, password):
    try:
        # Establish SSH connection
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(ip_address, username=username, password=password, timeout=5)

        # Start an interactive shell session
        shell = ssh_client.invoke_shell()

        # Send command to set terminal length to 0
        shell.send("terminal length 0\n")
        time.sleep(1)

        # Send command to show spanning-tree summary
        shell.send("show spanning-tree summary\n")
        time.sleep(2)

        # Send command to show spanning-tree root
        shell.send("show spanning-tree root\n")
        time.sleep(2)


        # Read the output
        output = shell.recv(65535).decode()

        # Close SSH session
        ssh_client.close()

        return output

    except paramiko.AuthenticationException:
        return "Authentication failed. Please verify your credentials."
    except paramiko.SSHException as ssh_ex:
        return f"SSH error: {ssh_ex}"
    except Exception as ex:
        return f"Error: {ex}"


def save_output_to_file(output, filename):
    with open(filename, "w") as file:
        file.write(output)


# Function to read IPs from a file
def read_ips(filename):
    with open(filename, 'r') as file:
        ips = [line.strip() for line in file.readlines() if line.strip()]
    return ips


if __name__ == "__main__":
    # Define a list of switches with their credentials and IP addresses
    # Read switch IPs from a file
    switch_ips = read_ips('switch_ips.txt')
    print(switch_ips)

    switch_username = "username"  # Update with your username
    switch_password = "password"  # Update with your password

    for switch in switch_ips:
        # Log into the switch and retrieve output
        output = cisco_switch_login(switch, switch_username, switch_password)
        print(output)
        print(switch)

        # Get the current date and time
        current_datetime = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

        # Save output to a text file with switch hostname
        switch_hostname = input("Enter the hostname: ")
        filename = f"{switch_hostname}_spanning_tree_summary_{current_datetime}.txt"
        save_output_to_file(output, filename)

        print(f"Output for {switch_hostname} saved to {filename}")