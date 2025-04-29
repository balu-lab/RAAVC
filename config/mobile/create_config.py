import os
import json

CONFIG_PATH = "/home/raavc/RAAVC-local/config/raavc_config.json"

def ensure_directories_exist(path):
    dir_path = os.path.dirname(path)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def prompt_user_info():
    device_role = input("Enter device role (e.g., vent sensor): ").strip()
    device_location = input("Enter device location (e.g., living room vent): ").strip()
    wifi_ssid = input("Enter home WiFi SSID: ").strip()
    wifi_pass = input("Enter home WiFi password: ").strip()

    return {
        "device_role": device_role,
        "device_location": device_location,
        "wifi_ssid": wifi_ssid,
        "wifi_pass": wifi_pass
    }

def write_config_file(path, config_data):
    with open(path, 'w') as f:
        json.dump(config_data, f, indent=4)

def main():
    if os.path.exists(CONFIG_PATH):
        print(f"Config already exists at {CONFIG_PATH}")
        return

    ensure_directories_exist(CONFIG_PATH)
    config_data = prompt_user_info()
    write_config_file(CONFIG_PATH, config_data)
    print(f"Configuration written to {CONFIG_PATH}")

if __name__ == "__main__":
    main()