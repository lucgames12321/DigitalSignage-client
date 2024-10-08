# Digital Signage Client

## Description

This project contains a Python script designed to open a webpage on the chromium-browser installed on any linux distro. The script will try to:
- Open Chromium Browser with provided link you input in the script when prompted
- Opens Chromium Browser in fullscreen (Kiosk mode).
- Will display notifications set within the script to show on top of the full screen windows.


## Installation

### 1. Clone the repository:
```bash
    git clone https://github.com/lucgames12321/DigitalSignage-client.git
```
### 2. Navigate to the project directory:
```bash
    cd DigitalSignage-client
```
### 3. (Optional) Create and activate a virtual environment:
```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 4. Install the required dependencies:
```bash
    sudo apt-get update && sudo apt-get upgrade -y
    sudo apt install python3 python3-tk python3-webview xdotool chromium-browser
```

   - `python3` - Used for the script.
   - `python3-tk` - Tkinter package used for the notifications.
   - `python3-webview` - Used for displaying web apps in the notification bar.
   - `xdotool` - used for doing keypresses in the background to change the URL, etc.
   - `chromium-browser` - Used as browser for displaying the webpages.

    
### 5. Also reccomended:
```bash
    sudo apt install unclutter
```

   - `unclutter` - Used for automaticly removing the cursor from the screen.



## Usage

To run the script, use the following command:
```bash
python3 script_name.py
```


## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or suggestions, please contact DonerNator.
