#!/bin/bash

DEVICE_NAME="New RAAVC Device"
CONFIG_DIR="config"
INCOMING_DIR="$HOME/bluetooth"

mkdir -p "$CONFIG_DIR"
mkdir -p "$INCOMING_DIR"

log() {
  echo "[$(date --iso-8601=seconds)] $1"
}

set_bluetooth() {
  bluetoothctl << EOF
power on
system-alias $DEVICE_NAME
agent NoInputNoOutput
discoverable on
pairable on
default-agent
EOF
}

wait_for_file() {
  local filename=$1
  local timeout=60
  local elapsed=0

  log "Waiting for $filename to arrive in $INCOMING_DIR..."
  while [ $elapsed -lt $timeout ]; do
    if [ -f "$INCOMING_DIR/$filename" ]; then
      log "$filename received."
      return 0
    fi
    sleep 1
    ((elapsed++))
  done
  log "Timeout waiting for $filename."
  return 1
}

main() {
  set_bluetooth
  log "RAAVC Bluetooth Provisioner ready."
  log "Ensure Bluetooth is discoverable and sending to $INCOMING_DIR."

  wait_for_file "raavc_config.json" && mv "$INCOMING_DIR/raavc_config.json" "$CONFIG_DIR/" && log "Config file moved to $CONFIG_DIR."
  wait_for_file "wifi_creds.json" && mv "$INCOMING_DIR/wifi_creds.json" "$CONFIG_DIR/" && log "WiFi credentials file moved to $CONFIG_DIR."
}

main