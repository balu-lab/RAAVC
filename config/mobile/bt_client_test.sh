#!/bin/bash

TARGET_NAME="New RAAVC Device"
RFCOMM_DEV="/dev/rfcomm0"

echo "[CLIENT] Scanning for '$TARGET_NAME'..."

TARGET_ADDR=$(bluetoothctl devices | grep "$TARGET_NAME" | awk '{print $2}')

if [ -z "$TARGET_ADDR" ]; then
    echo "[CLIENT] Device not known. Scanning..."
    bluetoothctl --timeout 10 scan on
    TARGET_ADDR=$(bluetoothctl devices | grep "$TARGET_NAME" | awk '{print $2}')
fi

if [ -z "$TARGET_ADDR" ]; then
    echo "[CLIENT] Device '$TARGET_NAME' not found."
    exit 1
fi

echo "[CLIENT] Found $TARGET_NAME at $TARGET_ADDR"

# Optional: pair and trust
echo -e "pair $TARGET_ADDR\ntrust $TARGET_ADDR\nquit" | bluetoothctl

# Release if already bound
sudo rfcomm release 0 &>/dev/null

# Connect to the target via RFCOMM
echo "[CLIENT] Connecting to $TARGET_ADDR on RFCOMM channel 1..."
sudo rfcomm connect 0 $TARGET_ADDR 1 &
sleep 5

if [ -e "$RFCOMM_DEV" ]; then
    echo "[CLIENT] Connected. Sending test message..."
    echo "Hello from client!" | sudo tee "$RFCOMM_DEV" > /dev/null
    sleep 1
    sudo rfcomm release 0
    echo "[CLIENT] Done."
else
    echo "[CLIENT] Failed to connect to RFCOMM."
fi