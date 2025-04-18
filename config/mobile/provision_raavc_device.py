import json
import time
from datetime import datetime
import bluetooth

def log(msg):
    print(f"[{datetime.now().isoformat()}] {msg}")

def prompt_raavc_config():
    device_id = input("Enter device ID (e.g. VENT_1038): ").strip()
    role = input("Enter role (vent / sensor / master): ").strip().lower()
    room = input("Enter room name: ").strip()

    config = {
        "device_id": device_id,
        "role": role,
        "room": room
    }

    if role in ["vent", "sensor"]:
        min_temp = float(input("Enter minimum temp threshold: ").strip())
        max_temp = float(input("Enter maximum temp threshold: ").strip())
        config["thresholds"] = {
            "min": min_temp,
            "max": max_temp
        }

    return config

def prompt_wifi_creds():
    ssid = input("Enter WiFi SSID: ").strip()
    password = input("Enter WiFi password: ").strip()

    return {
        "ssid": ssid,
        "password": password
    }

def find_target_device(target_name):
    log(f"Scanning for Bluetooth devices named '{target_name}'...")
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True)
    for addr, name in nearby_devices:
        print(f"Found: {name} ({addr})")
        if name == target_name:
            return addr
    return None

def main():
    TARGET_NAME = "New RAAVC Device"
    target_addr = find_target_device(TARGET_NAME)

    if not target_addr:
        log("Target device not found.")
        return

    log(f"Connecting to {target_addr} via RFCOMM...")
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((target_addr, 1))

    log("Prompting for provisioning data...")
    raavc_config = prompt_raavc_config()
    wifi_creds = prompt_wifi_creds()

    full_package = {
        "config": raavc_config,
        "wifi": wifi_creds
    }

    # Send as one JSON payload
    payload = json.dumps(full_package).encode("utf-8")
    sock.send(payload)

    sock.close()
    log("Provisioning data sent.")

if __name__ == "__main__":
    main()