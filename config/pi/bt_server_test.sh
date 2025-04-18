#!/bin/bash

DEVICE_NAME="New RAAVC Device"
RFCOMM_DEVICE="/dev/rfcomm0"
OUTPUT_FILE="received_data.txt"

# Set Bluetooth name and make discoverable/pairable
bluetoothctl << EOF
power on
system-alias $DEVICE_NAME
agent NoInputNoOutput
discoverable on
pairable on
default-agent
EOF

echo "[INFO] Bluetooth device configured as '$DEVICE_NAME'."
echo "[INFO] Starting RFCOMM listener on channel 1..."

# Kill any existing rfcomm connections
sudo rfcomm release 0 2>/dev/null

# Listen for incoming connection (binds /dev/rfcomm0)
sudo rfcomm listen hci0 1 &
RFCOMM_PID=$!

# Wait for /dev/rfcomm0 to be created
while [ ! -e "$RFCOMM_DEVICE" ]; do
    sleep 1
done

echo "[INFO] Connection established. Waiting for data..."

# Read data from /dev/rfcomm0 and write to file
cat "$RFCOMM_DEVICE" > "$OUTPUT_FILE"

# Cleanup
sudo rfcomm release 0
kill "$RFCOMM_PID"

echo "[INFO] Data saved to $OUTPUT_FILE"