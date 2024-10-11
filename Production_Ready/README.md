
- Chromium browser als main broswer
- Cookies uit gezet van derden
- **Translator uitgezet!!!**



# unclutter geinstalleerd om de muis te laten verdwijnen
`sudo apt install unclutter` en daarna via `sudo raspi-config > Advanced > A6 Wayland > X11` en daarna op finish. Nu moet de pi rebooten via het bericht in het scherm.

> Als dit niet gedaan wordt dan gaat de muis niet weg alleen als de graphics driver op X11 staat!

aan het startup file--> `sudo nano /etc/xdg/lxsession/LXDE-pi/autostart` heb ik de volgende command toegevoegd aan het einde: `@unclutter -idle 1` om na 1 seconde de muis van het scherm te halen.




# Dit is allemaal overbodig voor de PI 5 
voor errors weg te halen:
```bash
sudo apt install mesa-utils mesa-vulkan-drivers
sudo apt install libgbm1
sudo apt install python3-psutil



# We hebben de gpu memory allocation aangepast naar 256
sudo nano /boot/config.txt
# voeg het volgende toe aan dit bestand
gpu_mem=256
