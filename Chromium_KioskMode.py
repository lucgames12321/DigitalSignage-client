import subprocess

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

try:
    # Run the command
    subprocess.run(chromium_command)
except Exception as e:
    print(f"Error running Chromium in kiosk mode: {e}")
