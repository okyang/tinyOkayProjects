#!/bin/bash

# Author: Owen Yang
# Notes: This bash script is meant to run the pir_activated_cam.py script from any folder. This was mainly
# created so that the .desktop file can run the script on startup if needed.

cd {}

echo "Running pir_actiavted_cam"

python3 pir_activated_cam.py
