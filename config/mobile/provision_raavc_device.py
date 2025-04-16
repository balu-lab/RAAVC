import json
import time
from datetime import datetime
import paho.mqtt.publish as publish

CONFIG_TOPIC = "raavc/config"
WIFI_TOPIC = "raavc/wifi"

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

def send_via_mqtt(broker_ip, topic, payload, label):
    try:
        publish.single(topic, json.dumps(payload), hostname=broker_ip)
        log(f"{label} sent successfully to topic '{topic}'")
        return True
    except Exception as e:
        log(f"Error sending {label}: {e}")
        return False

def main():
    broker_ip = input("Enter the Pi's MQTT broker IP address: ").strip()

    log("Prompting for provisioning data...")
    raavc_config = prompt_raavc_config()
    wifi_creds = prompt_wifi_creds()

    time.sleep(1)
    if not send_via_mqtt(broker_ip, CONFIG_TOPIC, raavc_config, "RAAVC config"):
        return

    time.sleep(1)
    send_via_mqtt(broker_ip, WIFI_TOPIC, wifi_creds, "WiFi credentials")

if __name__ == "__main__":
    main()
