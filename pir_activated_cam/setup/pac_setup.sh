#!/bin/bash

echo "Installing xterminal"
sudo apt-get install xterm -y
echo "Done"
echo

echo "Installing nanPy"
pip3 install nanPy -y
echo "Done"
echo

echo "Installing Arduino"
sudo apt-get install arduino -y
echo "Done"
echo

echo "Making Dependent files"
python3 makeDependentFiles.py
echo "Done"
echo


echo "Setting up .desktop file"
mkdir /home/pi/.config/autostart
cp pac_startup.desktop /home/pi/.config/autostart/pac_startup.desktop
echo "Done"
echo
