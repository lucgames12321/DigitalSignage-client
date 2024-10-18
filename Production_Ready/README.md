
# DigitalSignage Client - Production Ready
In this file you will find the configuration steps used to setup a Raspberry PI for DigitalSignage.

## Browser Configuration
- Chromium browser as the main browser
- Third-party cookies disabled
- Install extensions like Adblock and accept cookies
- **Translator disabled!!!**

## Configure Raspberry Pi Settings
Use `raspi-config` to configure essential settings:
- **System Options**: Change the hostname to your preferred name.
- **Display Options**: Disable screen blanking to prevent the screen from turning off.
- **Interface Options**: Enable SSH for remote access.
- **Advanced Options**: Expand the filesystem to use the full SD card capacity.
- **Advanced Options**: If not already set, configure Wayland to use X11.

> Note: After making these changes, select "Finish" and reboot your Raspberry Pi when prompted.



## Install Dependencies and xdotool
To ensure your Raspberry Pi is up to date and has all necessary dependencies for running this project, run the following commands:
```bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt install python3 python3-tk python3-webview xdotool unclutter chromium-browser
sudo reboot
```



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



# Dit stuk moet nog gerevamped worden:






## Change boot screen logo
Voor de RPI wordt er gebruik gemaakt van `plymouyh` voor de bootscreen manager
`/usr/share/plymouth/themes/pix` is waar de splashcreen vervangen moet worden.
















# Additional Configuration for PI 4 (Not needed for the PI 5)
To remove errors, install the following packages:
```bash
sudo apt install mesa-utils mesa-vulkan-drivers
sudo apt install libgbm1
sudo apt install python3-psutil
```

## GPU Memory Allocation (Optional)
We only need to do this step if your using PI 4, because they allocate not sufficient GPU Memory.
We have adjusted the GPU memory allocation to 256MB:
```bash
sudo nano /boot/firmware/config.txt
```
Add the following line to the file:
```bash
gpu_mem=256
```
