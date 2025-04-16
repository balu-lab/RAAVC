#!/bin/bash

CONFIG_PATH="/raavc/config/raavc_config.json"

# Check if config file exists
if [ -f "$CONFIG_PATH" ]; then
    echo "Config file found: $CONFIG_PATH"

    # Extract the role value using jq
    ROLE=$(jq -r '.role // empty' "$CONFIG_PATH")

    if [ -z "$ROLE" ]; then
        echo "Role not set in config. Running setup..."
        python3 setup.py
    fi
else
    echo "Config file not found. Running setup..."
    python3 setup.py
fi