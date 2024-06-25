#!/bin/bash

# Optional: Set up a virtual environment
 python3 -m venv venv
 source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Restart your application/service (example using systemd)
sudo systemctl restart main
