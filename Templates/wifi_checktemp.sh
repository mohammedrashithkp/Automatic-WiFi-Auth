#!/bin/bash
SSID_LIST=("SSID1" "SSID2" "SSID3")  # Replace with your Wi-Fi names
CURRENT_SSID=$(nmcli -t -f active,ssid dev wifi | grep '^yes' | cut -d: -f2)

if [[ " ${SSID_LIST[@]} " =~ " ${CURRENT_SSID} " ]]; then
    python3 /path/to/your_script.py  # Replace with your Python script
fi
