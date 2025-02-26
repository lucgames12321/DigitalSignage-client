import socketio
import subprocess
import socket
import os

# Create a Socket.IO client instance
sio = socketio.Client()

device_name = socket.gethostname()

# Path to Chromium executable (this is the standard path on Raspberry Pi)
chromium_path = "chromium-browser"

# Event handler for connection
@sio.event
def connect():
    print("Connected to the server")
    # Send the unique ID to register this device
    sio.emit('register', {'id': device_name})

# Event handler for disconnection
@sio.event
def disconnect():
    print("Disconnected from server")

# Event handler for update-url event
@sio.on('update-url')
def on_update_url(data):
    print(f"Received new URL: {data['url']}")
    # Command to open the new URL in Chromium
    with open(os.devnull, 'w') as devnull:
        subprocess.run(
            [chromium_path, "--noerrdialogs", "--disable-infobars", "--kiosk", data['url']],
            stderr=devnull  # Redirect stderr to /dev/null
        )

# Connect to the Socket.IO server
sio.connect('http://10.90.1.1:8003')

# Keep the client running
sio.wait()

