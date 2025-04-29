print("[PYTHON] Hello from boot_entry.py!")

import os
import subprocess
import time
import socket

CONFIG_PATH = "/home/raavc/RAAVC-local/config/raavc_config.json"

def get_ip():
    try:
        # Get first non-localhost IPv4 address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return None

def configure_bluetooth():
    try:
        bt_commands = (
            "power on\n"
            "agent NoInputNoOutput\n"
            "default-agent\n"
            "pairable on\n"
            "discoverable on\n"
        )
        subprocess.run(['bluetoothctl'], input=bt_commands.encode(), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Bluetooth setup error: {e}")

def set_bluetooth_alias(alias):
    try:
        subprocess.run(['bluetoothctl', 'system-alias', alias], check=True)
    except subprocess.CalledProcessError:
        pass

def main():
    configure_bluetooth()

    last_ip = None

    while not os.path.exists(CONFIG_PATH):
        ip = get_ip()
        if ip and ip != last_ip:
            set_bluetooth_alias(f"RAAVC-{ip}")
            print("[PYTHON] Check BT devices for IP address now.")
            last_ip = ip
        time.sleep(30)  # Wait and recheck

if __name__ == "__main__":
    main()