import json
import time
from datetime import datetime
import bluetooth
import os

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

def send_file_via_bluetooth(bt_addr, file_path):
    try:
        os.system(f'obexftp --nopath --noconn --uuid none --bluetooth {bt_addr} --channel 9 --put "{file_path}"')
        log(f"File '{file_path}' sent successfully via Bluetooth to {bt_addr}")
        return True
    except Exception as e:
        log(f"Error sending file via Bluetooth: {e}")
        return False

def main():
    TARGET_NAME = "New RAAVC Device"
    log(f"Scanning for Bluetooth devices named '{TARGET_NAME}'...")
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True)

    bt_addr = None
    for addr, name in nearby_devices:
        print(name)
        if name == TARGET_NAME:
            bt_addr = addr
            break

    if not bt_addr:
        log(f"Device named '{TARGET_NAME}' not found.")
        return

    log(f"Found target device at {bt_addr}")

    log("Prompting for provisioning data...")
    raavc_config = prompt_raavc_config()
    wifi_creds = prompt_wifi_creds()

    with open("raavc_config.json", "w") as f:
        json.dump(raavc_config, f)

    with open("wifi_creds.json", "w") as f:
        json.dump(wifi_creds, f)

    time.sleep(1)
    send_file_via_bluetooth(bt_addr, "raavc_config.json")

    time.sleep(1)
    send_file_via_bluetooth(bt_addr, "wifi_creds.json")

if __name__ == "__main__":
    main()