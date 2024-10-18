import subprocess

def scan_wifi():
    try:
        # Run the 'nmcli' command to scan for available Wi-Fi networks
        result = subprocess.run(['nmcli', 'dev', 'wifi'], capture_output=True, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            print("Available Wi-Fi networks:")
            print(result.stdout)
        
            # Await user input for SSID
            ssid = input("Enter the SSID of the network you want to connect to: ")

            # Await user input for password (skip if network is open)
            password = input("Enter the Wi-Fi password (leave blank if the network is open): ")

            # Connect to the Wi-Fi network
            connect_to_wifi(ssid, password)

        else:
            print("Error scanning for networks:")
            print(result.stderr)

    except Exception as e:
        print(f"An error occurred: {e}")

def connect_to_wifi(ssid, password):
    try:
        # Check if password is provided (open network vs secured)
        if password:
            # Connect to the network using the provided SSID and password
            command = ['nmcli', 'dev', 'wifi', 'connect', ssid, 'password', password]
        else:
            # Connect to the open network (no password)
            command = ['nmcli', 'dev', 'wifi', 'connect', ssid]

        # Execute the command to connect to the Wi-Fi network
        result = subprocess.run(command, capture_output=True, text=True)

        # Check if the connection was successful
        if result.returncode == 0:
            print(f"Successfully connected to {ssid}!")
        else:
            print(f"Failed to connect to {ssid}:")
            print(result.stderr)

    except Exception as e:
        print(f"An error occurred while trying to connect: {e}")


# Run the function to scan Wi-Fi networks
scan_wifi()

