import os
import shutil
from pathlib import Path
from datetime import datetime

CONFIG_DIR = Path("/RAAVC/config")
CONFIG_DIR.mkdir(parents=True, exist_ok=True)

INCOMING_DIR = Path.home() / "bluetooth"
INCOMING_DIR.mkdir(parents=True, exist_ok=True)

def log(msg):
    print(f"[{datetime.now().isoformat()}] {msg}")

def wait_for_file(filename, timeout=60):
    log(f"Waiting for {filename} to arrive in Bluetooth folder...")
    elapsed = 0
    while elapsed < timeout:
        target_path = INCOMING_DIR / filename
        if target_path.exists():
            log(f"{filename} received.")
            return target_path
        time.sleep(1)
        elapsed += 1
    log(f"Timeout waiting for {filename}.")
    return None

def main():
    log("RAAVC Bluetooth Provisioner ready.")
    log(f"Ensure Bluetooth is discoverable and waiting for file transfer to {INCOMING_DIR}.")

    config_path = wait_for_file("raavc_config.json")
    wifi_path = wait_for_file("wifi_creds.json")

    if config_path:
        shutil.move(str(config_path), CONFIG_DIR / "raavc_config.json")
        log("Config file moved to RAAVC config directory.")

    if wifi_path:
        shutil.move(str(wifi_path), CONFIG_DIR / "wifi_creds.json")
        log("WiFi credentials file moved to RAAVC config directory.")

if __name__ == "__main__":
    import time
    main()