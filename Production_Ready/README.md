
# DigitalSignage Client - Production Ready
In this file you will find the configuration steps used to setup a Raspberry PI for DigitalSignage.

-----------------------------------------------------------------------
## Easy Install Script

To simplify the installation process, you can use the provided `setup.sh` script. Follow these steps to download and execute it on your Raspberry Pi 5:

1. Open a terminal on your Raspberry Pi.
2. Clone the repository containing the `setup.sh` script:

    ```bash
    git clone https://github.com/lucgames12321/DigitalSignage-client.git
    ```

4. Navigate to the directory containing the script:

    ```bash
    cd DigitalSignage-client/Production_Ready
    ```
    
6. Make the script executable:

    ```bash
    chmod +x setup.sh
    ```
    
8. Run the script:

    ```bash
    ./setup.sh
    ```
    

This script will automatically install all necessary dependencies and configure your Raspberry Pi for DigitalSignage.

-----------------------------------------------------------------------
## Configure Raspberry Pi Settings
Use `raspi-config` to configure essential settings:
- **System Options**: Change the hostname to your preferred name.
- **Display Options**: Disable screen blanking to prevent the screen from turning off.
- **Interface Options**: Enable SSH for remote access.
- **Advanced Options**: Expand the filesystem to use the full SD card capacity.
- **Advanced Options**: If not already set, configure Wayland to use X11.

> Note: After making these changes, select "Finish" and reboot your Raspberry Pi when prompted.

-----------------------------------------------------------------------
## Browser Configuration
- Chromium browser as the main browser
- Third-party cookies disabled
- Install extensions like Adblock and accept cookies
- **Translator disabled!!!**

-----------------------------------------------------------------------
## Install Dependencies and xdotool
To ensure your Raspberry Pi is up to date and has all necessary dependencies for running this project, run the following commands:
```bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt install python3 python3-socketio python3-subprocess-tee python3-websocket xdotool unclutter chromium-browser
sudo reboot
```
-----------------------------------------------------------------------
## Automate python script
These steps are needed to run the Kiosk-client.py in the background as a systemctl service.

### Create the Python script

Create the Python script in the following directory:
```sh
nano /home/ds0X/Documents/kiosk_client.py
```

Make it executable:
```sh
chmod +x /home/ds0X/Documents/kiosk_client.py
```

### Create a new service file

Create a new service file:
```sh
sudo nano /etc/systemd/system/kiosk-client.service
```

Paste the following:
```ini
[Unit]
Description=Kiosk Client Service
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/ds0X/Documents/kiosk_client.py # REPLACE THIS WITH THE CORRECT USER
WorkingDirectory=/home/ds0X/Documents # REPLACE THIS WITH THE CORRECT USER
Restart=always
RestartSec=5
User=ds0X # REPLACE THIS WITH THE CORRECT USER
Environment=DISPLAY=:0
Environment=XDG_RUNTIME_DIR=/run/user/1000

[Install]
WantedBy=multi-user.target
```

### Enable and start the service

Reload the systemd manager configuration and enable the service:
```sh
sudo systemctl daemon-reload
sudo systemctl enable kiosk-client.service
sudo systemctl start kiosk-client.service
```

To Check the status of the service type the following:
```sh
sudo systemctl status kiosk-client.service
```

-----------------------------------------------------------------------
## Load default page on reboot
This will open a default webpage configured with these settings

### Edit the autostart file
To open a default URL on startup, edit the autostart file:
```sh
nano ~/.config/lxsession/LXDE-pi/autostart
```

Add this line at the end:
```sh
@chromium-browser --noerrdialogs --disable-infobars --kiosk https://threatmap.bitdefender.com/
```

### Reboot and test it
The DigitalSIgnage screen should now: start the python script in the background as a service calles ``kiosk-client.service`` and open Chrome in kiosk mode with the default page ``https://threatmap.bitdefender.com/``
```sh
sudo reboot
```

-----------------------------------------------------------------------
## Mouse Cursor Configuration
Unclutter is installed to hide the mouse cursor:
```bash
sudo apt install unclutter
```
**If not already done:** configure:
```bash
sudo raspi-config > Advanced > A6 Wayland > X11
```
Afterwards, select finish and reboot the Pi as prompted.

> Note: If this step is not completed, the mouse cursor will not disappear unless the graphics driver is set to X11!

**(Optional normally mouse disappears after 5 seconds)** Add the following command to the startup file to hide the mouse cursor after 1 second of inactivity:
```bash
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
**(Optional)** Append the following line at the end:
```bash
@unclutter -idle 1
```

-----------------------------------------------------------------------
## Additional Configuration for PI 4 (Not needed for the PI 5)
To remove errors, install the following packages:
```bash
sudo apt install mesa-utils mesa-vulkan-drivers
sudo apt install libgbm1
sudo apt install python3-psutil
```

### GPU Memory Allocation (Optional)
We only need to do this step if your using PI 4, because they allocate not sufficient GPU Memory.
We have adjusted the GPU memory allocation to 256MB:
```bash
sudo nano /boot/firmware/config.txt
```
Add the following line to the file:
```bash
gpu_mem=256
```
