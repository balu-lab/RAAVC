import json

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
        min_temp = float(input("Enter minimum temperature threshold: ").strip())
        max_temp = float(input("Enter maximum temperature threshold: ").strip())
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
    print("=== RAAVC Config Generator ===")
    raavc_config = prompt_raavc_config()
    wifi_creds = prompt_wifi_creds()

    with open("raavc_config.json", "w") as f:
        json.dump(raavc_config, f, indent=2)
    print("Saved raavc_config.json")

    with open("wifi_creds.json", "w") as f:
        json.dump(wifi_creds, f, indent=2)
    print("Saved wifi_creds.json")

if __name__ == "__main__":
    main()