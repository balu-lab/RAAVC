#!/bin/bash

REPO_PATH="/home/raavc/RAAVC"
BOOT_SCRIPT="$REPO_PATH/config/boot/boot_entry.py"
REPO_URL="https://github.com/balu-lab/RAAVC.git"

echo "[BOOT] Waiting for WiFi connection..."

# Wait until wlan0 has an IP
while ! ip a | grep -q "wlan0.*inet "; do
    echo "[BOOT] WiFi not connected. Retrying in 3s..."
    sleep 3
done

echo "[BOOT] WiFi connected."

# Ensure Git is installed
if ! command -v git &> /dev/null; then
    echo "[BOOT] Git not found. Installing..."
    sudo apt-get update -y
    sudo apt-get install -y git
fi

# Clone or update the repo
if [ ! -d "$REPO_PATH" ]; then
    echo "[BOOT] RAAVC repo not found. Cloning..."
    git clone "$REPO_URL" "$REPO_PATH"
else
    echo "[BOOT] RAAVC repo exists. Pulling updates..."
    cd "$REPO_PATH" || exit 1
    git reset --hard HEAD
    git pull origin main
fi

# Run the boot entry script
echo "[BOOT] Running boot_entry.py..."
python3 "$BOOT_SCRIPT"