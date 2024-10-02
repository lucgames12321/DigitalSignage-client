import subprocess
import os

# URL to open in Chromium
url = "https://www.example.com"

# Command to launch Chromium in kiosk mode
chromium_command = [
    "chromium-browser",
    "--kiosk",        # Kiosk mode (full screen without toolbars)
    "--noerrdialogs", # Suppresses error dialogs
    "--disable-infobars",  # Disable info bars
    "--incognito",    # Optional: opens Chromium in incognito mode
    "--disable-restore-session-state",  # Prevent session restoration prompts
    url
]

# Set the DISPLAY environment variable to :0
env = os.environ.copy()
env["DISPLAY"] = ":0"  # Target the Raspberry Pi's screen

try:
    # Run the command with the modified environment
    subprocess.run(chromium_command, env=env)
except Exception as e:
    print(f"Error running Chromium in kiosk mode: {e}")
