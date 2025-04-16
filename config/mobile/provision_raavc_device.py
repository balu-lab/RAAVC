import bluetooth
import json
import time
from pathlib import Path
from datetime import datetime

PI_BT_NAME = "New RAAVC Device"
CONFIG_PATH = Path("raavc_config.json")
WIFI_PATH = Path("wifi_creds.json")

def log(msg):
    print(f"[{datetime.now().isoformat()}] {msg}")

def find_pi_device():
    log("Scanning for Bluetooth devices...")
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True)

    for addr, name in nearby_devices:
        if name == PI_BT_NAME:
            log(f"Found RAAVC Pi at {addr}")
            return addr
    log("RAAVC Pi not found.")
    return None

def send_json_file(addr, json_data, label):
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        log(f"Connecting to {addr} for {label}...")
        sock.connect((addr, 1))  # Channel 1

        sock.send((json.dumps(json_data) + "\n").encode("utf-8"))
        log(f"{label} sent, waiting for response...")

        ack = sock.recv(1024).decode("utf-8").strip()
        if ack == "SUCCESS":
            log(f"{label} provisioning successful.")
            return True
        else:
            log(f"{label} provisioning failed: {ack}")
            return False
    except Exception as e:
        log(f"Error during {label} send: {e}")
        return False
    finally:
        sock.close()

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

def main():
    addr = find_pi_device()
    if not addr:
        return

    log("Bluetooth connection ready. Prompting for provisioning data...")

    raavc_config = prompt_raavc_config()
    wifi_creds = prompt_wifi_creds()

    time.sleep(1)
    if not send_json_file(addr, raavc_config, "RAAVC config"):
        return

    time.sleep(2)
    send_json_file(addr, wifi_creds, "WiFi credentials")

if __name__ == "__main__":
    main()