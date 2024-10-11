
# DigitalSignage Client - Production Ready

## Browser Configuration
- Chromium browser as the main browser
- Third-party cookies disabled
- **Translator disabled!!!**



## Mouse Cursor Configuration
Unclutter is installed to hide the mouse cursor:
```bash
sudo apt install unclutter
```
Then configure via:
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

# Additional Configuration for PI 4 (Not needed for the PI 5)
To remove errors, install the following packages:
```bash
sudo apt install mesa-utils mesa-vulkan-drivers
sudo apt install libgbm1
sudo apt install python3-psutil
```

## GPU Memory Allocation (Optional)
We only need to do this step if your using PI 4, because they allocate not sufficient GPU Memory
We have adjusted the GPU memory allocation to 256MB:
```bash
sudo nano /boot/config.txt
```
Add the following line to the file:
```bash
gpu_mem=256
```