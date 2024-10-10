import subprocess
import os

# Function to change the URL in the current Chromium instance
def change_url(new_url):
    # Command to focus on the Chromium window and replace the URL
    xdotool_commands = f"""
    xdotool search --onlyvisible --class chromium windowfocus
    xdotool key Ctrl+l
    xdotool type '{new_url}'
    xdotool key Return
    """

    # Execute the xdotool commands
    subprocess.run(xdotool_commands, shell=True)


# Function to check if Chromium is running
def is_chromium_running():
    try:
        # Use pgrep to check if any Chromium process is running
        result = subprocess.run(['pgrep', '-f', 'chromium-browser'], stdout=subprocess.PIPE)
        return result.returncode == 0  # return True if Chromium is running
    except Exception as e:
        print(f"Error checking Chromium process: {e}")
        return False



# Function to open Chromium in kiosk mode
def open_chromium(url):
    # Command to launch Chromium in kiosk mode
    chromium_command = [
        "chromium-browser",
        "--kiosk",        # Kiosk mode (full screen without toolbars)
        "--noerrdialogs", # Suppresses error dialogs
        "--disable-infobars",  # Disable info bars
        "--incognito",    # Optional: opens Chromium in incognito mode
        "--disable-restore-session-state",  # Prevent session restoration prompts
        "--disable-software-rasterizer", #Disable software rasterizer
        "--disable-features=VizDisplayCompositor",  # Disables the Viz compositor, can help on low-powered systems
        "--disable-dev-shm-usage",  # Prevents Chromium from using /dev/shm for shared memory (useful on Raspberry Pi)
        "--no-sandbox",  # Runs Chromium without the sandbox (not recommended for security but might help here)
        "--disable-background-timer-throttling",  # Disable background timer throttling (might prevent performance issues)
        "--disable-backgrounding-occluded-windows",  # Prevents backgrounding of non-visible windows (useful in kiosk mode)
        "--disable-breakpad",  # Disables the crash reporting (may avoid related crashes)
         "--use-fake-ui-for-media-stream",  # Avoid camera/microphone prompts
        "--disable-camera",  # Disable camera access
        url
    ]



    # Set the DISPLAY environment variable to :0
    env = os.environ.copy()
    env["DISPLAY"] = ":0"  # Target the Raspberry Pi's screen




    try:
        # Run the command with the modified environment to launch Chromium.
        subprocess.Popen(chromium_command, env=env)
    except Exception as e:
        print(f"Error running Chromium in kiosk mode: {e}")


# Main loop to continuously ask for new URLs
while True:
    # Prompt the user for a URL
    print("Geef een URL op om te openen (Voorbeeld: https://youtube.com) of type 'exit' om te stoppen:")
    url = input()

    # Exit condition
    if url.lower() == 'exit':
        print("Exiting the script.")
        break

    # Check if Chromium is already running
    if is_chromium_running():
        print("Chromium is running, changing the URL.")
        try:
            change_url(url)
        except Exception as e:
            print(f"Error changing URL: {e}")
    else:
        print("Launching Chromium.")
        open_chromium(url)
