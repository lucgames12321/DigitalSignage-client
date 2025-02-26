#!/bin/bash

# Check if the script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root (use sudo setup.sh)"
    exit 1
fi

# Script information
clear # Clear the terminal
echo "################################################################################"
echo "#                                                                              #"
echo "#                   Digital Signage Automatic Setup Script                     #"
echo "#                                Version 1.3.1                                 #"
echo "#                             Made by DonerNator                               #"
echo "#                                                                              #"
echo "################################################################################"
echo ""
echo "# This script will update and upgrade your system, install necessary packages, #"
echo "# and configure your Raspberry Pi.                                             #"
echo ""


# Check if the script has been run before
if [ -f "/var/log/digital_signage_setup.log" ]; then
    echo "Setup script has already been run. Skipping setup steps..."
    tail -n +119 "$0" | bash
    exit 0
fi

# Create a log file to indicate the script has been run
sudo touch /var/log/digital_signage_setup.log




# Ask for user input to proceed with installation
read -p "Do you want to proceed with the installation? (Y/n): " user_input
if [[ "$user_input" != "Y" && "$user_input" != "y" ]]; then
    clear # Clear the terminal
    echo "Installation aborted by user."
    exit 1
fi

# Update and upgrade the system with a progress bar
echo "Updating and upgrading the system..."
sudo apt-get update -y > /dev/null 2>&1 &
pid=$!
while ps -p $pid > /dev/null; do
    echo -n "."
    sleep 1
done
echo " Done."

sudo apt-get upgrade -y > /dev/null 2>&1 &
pid=$!
while ps -p $pid > /dev/null; do
    echo -n "."
    sleep 1
done
echo " Done."


# Install necessary packages
echo "Installing necessary packages..."
sudo apt install -y python3 python3-tk python3-webview python3-socketio python3-subprocess-tee xdotool unclutter chromium-browser > /dev/null 2>&1 &
pid=$!
while ps -p $pid > /dev/null; do
    echo -n "."
    sleep 1
done
echo " Done."



# Clear the terminal
clear
echo "Installation done."

# Change raspi-config settings
echo "##################Configuring Raspberry Pi settings##################"

# Change Wayland option to X11
echo "Changing Wayland option to X11..."
sudo raspi-config nonint do_x11

# Enable SSH
echo "Enabling SSH..."
sudo raspi-config nonint do_ssh 0

# Disable screen blanking
echo "Disabling screen blanking..."
sudo raspi-config nonint do_blanking 1

# Expand the filesystem to use the full SD card
echo "Expanding the filesystem..."
sudo raspi-config nonint do_expand_rootfs

# Change hostname
read -p "Enter the new hostname: " new_hostname
sudo raspi-config nonint do_hostname "$new_hostname"


# Configuration done message
clear
echo "Configuration done."


# Ask if the user wants to reboot
read -p "Do you want to reboot your Raspberry Pi now? (Y/n): " reboot_input
if [[ "$reboot_input" == "Y" || "$reboot_input" == "y" ]]; then
    sudo reboot
else
    echo "Please reboot your Raspberry Pi for changes to take effect."
fi



# Pull the script from the GitHub repository and set up a systemd service
echo "Setting up the Digital Signage service..."

# Define variables
REPO_URL="https://github.com/lucgames12321/DigitalSignage-client.git"
SERVICE_NAME="DigitalSignage"
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME.service"

# Clone the repository
if [ ! -d "/opt/$SERVICE_NAME" ]; then
    sudo git clone $REPO_URL /opt/$SERVICE_NAME
else
    echo "Repository already cloned. Pulling latest changes..."
    sudo git -C /opt/$SERVICE_NAME pull
fi

# Create the systemd service file
sudo bash -c "cat > $SERVICE_FILE" <<EOL
[Unit]
Description=Digital Signage Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /opt/$SERVICE_NAME/Production_Ready/raspberrypi_kiosk.py
WorkingDirectory=/opt/$SERVICE_NAME/Production_Ready
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd, enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable $SERVICE_NAME
sudo systemctl start $SERVICE_NAME

clear
echo "Digital Signage service setup complete."


# Script done running
echo "Script done running. Everything is ready to go! Exiting..."
echo "If you want to run the script again, please delete the /var/log/digital_signage_setup.log file."
echo "If you have any questions or issues, please contact me on GitHub: DonerNator"
echo "Thank you for using the Digital Signage Automatic Setup Script."
echo "type sudo systemctl status DigitalSignage to check the status of the service"
echo "Exiting..."