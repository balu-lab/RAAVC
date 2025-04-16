import json
from pathlib import Path
from datetime import datetime
import paho.mqtt.client as mqtt

CONFIG_DIR = Path("config")
CONFIG_DIR.mkdir(parents=True, exist_ok=True)

RAAVC_CONFIG_PATH = CONFIG_DIR / "raavc_config.json"
WIFI_CREDS_PATH = CONFIG_DIR / "wifi_creds.json"

def log(msg):
    print(f"[{datetime.now().isoformat()}] {msg}")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        log("Connected to MQTT broker.")
        client.subscribe("raavc/config")
        client.subscribe("raavc/wifi")
        log("Subscribed to provisioning topics.")
    else:
        log(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        if msg.topic == "raavc/config":
            with open(RAAVC_CONFIG_PATH, "w") as f:
                json.dump(payload, f, indent=2)
            log("Saved raavc_config.json")
        elif msg.topic == "raavc/wifi":
            with open(WIFI_CREDS_PATH, "w") as f:
                json.dump(payload, f, indent=2)
            log("Saved wifi_creds.json")
    except Exception as e:
        log(f"Failed to process message on {msg.topic}: {e}")

def main():
    log("Starting RAAVC MQTT provisioning listener...")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Connect to local broker running on the Pi
    client.connect("localhost", 1883, 60)
    client.loop_forever()

if __name__ == "__main__":
    main()
