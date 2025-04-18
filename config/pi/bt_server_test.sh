#!/bin/bash

DEVICE_NAME="New RAAVC Device"
RFCOMM_CHANNEL=26
RFCOMM_DEVICE="/dev/rfcomm0"
OUTPUT_FILE="received_data.txt"

echo "[INFO] Releasing any existing RFCOMM bindings..."
sudo rfcomm release 0 &>/dev/null

# Kill lingering rfcomm listeners from previous runs on channel 26
EXISTING_PID=$(pgrep -f "rfcomm listen hci0 $RFCOMM_CHANNEL")
if [ -n "$EXISTING_PID" ]; then
  echo "[INFO] Killing existing rfcomm listener (PID $EXISTING_PID)..."
  sudo kill "$EXISTING_PID"
fi

# Set Bluetooth name and make discoverable/pairable
echo "[INFO] Configuring Bluetooth device..."
bluetoothctl << EOF
power on
system-alias $DEVICE_NAME
agent NoInputNoOutput
discoverable on
pairable on
default-agent
EOF

echo "[INFO] Bluetooth device set to '$DEVICE_NAME'."
echo "[INFO] Starting RFCOMM listener on channel $RFCOMM_CHANNEL..."

sudo rfcomm listen hci0 $RFCOMM_CHANNEL &
RFCOMM_PID=$!

# Wait for /dev/rfcomm0 to be created
echo "[INFO] Waiting for connection on /dev/rfcomm0..."
while [ ! -e "$RFCOMM_DEVICE" ]; do
    sleep 1
done

echo "[INFO] Connection established. Receiving data..."

# Read data from /dev/rfcomm0 and write to file
cat "$RFCOMM_DEVICE" > "$OUTPUT_FILE"

# Cleanup
echo "[INFO] Cleaning up..."
sudo rfcomm release 0 &>/dev/null
kill "$RFCOMM_PID" &>/dev/null

echo "[INFO] Data saved to $OUTPUT_FILE"