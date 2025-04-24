#!/bin/bash

export USER="raavc"
export HOME="/home/raavc"

REPO_PATH="/home/raavc/RAAVC"
BOOT_SCRIPT="$REPO_PATH/config/boot/boot_entry.py"
REPO_URL="https://github.com/balu-lab/RAAVC.git"
CONFIG_PATH="home/raavc/RAAVC-local/config/raavc_config.json"

echo "[BOOT] Checking for WiFi configuration..."

# Check for raavc_config.json and attempt WiFi connection
WIFI_WAIT=0
if [ -f "$CONFIG_PATH" ]; then
    SSID=$(jq -r '.wifi_ssid // empty' "$CONFIG_PATH")
    PASS=$(jq -r '.wifi_pass // empty' "$CONFIG_PATH")
    if [ -n "$SSID" ] && [ -n "$PASS" ]; then
        echo "[BOOT] Found WiFi in config. Attempting to connect to $SSID..."
        ATTEMPT=1
        CONNECTED=0
        while [ $ATTEMPT -le 4 ]; do
            nmcli device wifi connect "$SSID" password "$PASS"
            # Give a second for DHCP to assign an IP
            sleep 2
            if [ -n "$(hostname -I)" ]; then
                CONNECTED=1
                break
            else
                echo "[BOOT] Attempt $ATTEMPT failed to connect to $SSID."
            fi
            ATTEMPT=$((ATTEMPT+1))
        done
        if [ $CONNECTED -eq 1 ]; then
            # Extract and echo role from config if present
            ROLE=$(jq -r '.role // empty' "$CONFIG_PATH")
            if [ -n "$ROLE" ]; then
                echo "simulated $ROLE script running now"
            else
                echo "No role specified in config."
            fi
        else
            echo "[BOOT] All attempts failed. Will wait for any WiFi..."
            WIFI_WAIT=1
        fi
    else
        echo "[BOOT] Config present but no WiFi credentials. Waiting for any WiFi..."
        WIFI_WAIT=1
    fi
else
    echo "[BOOT] No config file; waiting for any WiFi connection (e.g., default hotspot)."
    WIFI_WAIT=1
fi

if [ $WIFI_WAIT -eq 1 ]; then
    echo "[BOOT] Waiting for WiFi connection..."
    while [ -z "$(hostname -I)" ]; do
        sleep 1
    done
    echo "[BOOT] WiFi connected."
    # If we want to still output the role if config present after default connect, do it here
    if [ -f "$CONFIG_PATH" ]; then
        ROLE=$(jq -r '.role // empty' "$CONFIG_PATH")
        if [ -n "$ROLE" ]; then
            echo "simulated $ROLE script running now"
        else
            echo "No role specified in config."
        fi
    fi
fi

# Ensure Git is installed
if ! command -v git &> /dev/null; then
    echo "[BOOT] Git not found. Installing..."
    sudo apt-get update -y
    sudo apt-get install -y git
fi

# Allow Git to trust this repo path (fixes "dubious ownership" warning)
git config --global --add safe.directory "$REPO_PATH"

# Clone or update the repo
if [ ! -d "$REPO_PATH" ]; then
    echo "[BOOT] RAAVC repo not found. Cloning..."
    git clone "$REPO_URL" "$REPO_PATH"
else
    echo "[BOOT] RAAVC repo found. Pulling updates..."
    cd "$REPO_PATH" || exit 1
    git reset --hard HEAD
    git pull origin main
fi

# Run the boot entry script
echo "[BOOT] Running boot_entry.py..."
python3 "$BOOT_SCRIPT"