###############################################################################
#
# Reboot the system, if it is not windows it will do it for linux and mac
#
###############################################################################



import os
import platform
import subprocess

def reboot_system():
    current_os = platform.system()
    
    try:
        if current_os == "Windows":
            # Windows reboot command
            subprocess.run(["shutdown", "/r", "/t", "0"], check=True)
        elif current_os == "Linux" or current_os == "Darwin":  # Darwin is macOS
            # Linux and macOS reboot command
            subprocess.run(["sudo", "reboot"], check=True)
        else:
            print(f"Unsupported OS: {current_os}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to reboot: {e}")

if __name__ == "__main__":
    reboot_system()
