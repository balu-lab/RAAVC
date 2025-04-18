#!/bin/bash

DEVICE_NAME="New RAAVC Device"
OUTPUT_FILE="received_data.txt"

while true; do
    echo "[INFO] Releasing any existing RFCOMM bindings..."
    sudo rfcomm release 0 &>/dev/null

    echo "[INFO] Configuring Bluetooth device for headless auto-pairing..."
    bluetoothctl << EOF
power on
agent NoInputNoOutput
default-agent
pairable on
discoverable on
system-alias $DEVICE_NAME
EOF

    # Find an available RFCOMM channel (fallback to 26 if unknown)
    RFCOMM_CHANNEL=$(shuf -i 10-30 -n 1)
    echo "[INFO] Using RFCOMM channel $RFCOMM_CHANNEL..."

    echo "[INFO] Starting RFCOMM listener on channel $RFCOMM_CHANNEL..."
    sudo rfcomm listen hci0 $RFCOMM_CHANNEL &
    RFCOMM_PID=$!

    # Wait for connection (file created means something connected)
    echo "[INFO] Waiting for incoming connection (/dev/rfcomm0)..."
    TIMEOUT=60
    TIMER=0
    while [ ! -e "/dev/rfcomm0" ] && [ $TIMER -lt $TIMEOUT ]; do
        sleep 1
        ((TIMER++))
    done

    if [ ! -e "/dev/rfcomm0" ]; then
        echo "[WARN] No connection established after $TIMEOUT seconds. Retrying..."
        kill "$RFCOMM_PID" &>/dev/null
        continue
    fi

    echo "[INFO] Connection established. Receiving data..."
    cat /dev/rfcomm0 > "$OUTPUT_FILE"

    echo "[INFO] Data saved to $OUTPUT_FILE"
    echo "[INFO] Resetting and waiting for new connection..."

    sudo rfcomm release 0 &>/dev/null
    kill "$RFCOMM_PID" &>/dev/null

    sleep 2
done