import webview
import tkinter as tk

# Get the screen dimensions using tkinter
root = tk.Tk()
root.withdraw()  # Hide the root window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


# Set window transparency (0.0 = fully transparent, 1.0 = fully opaque)
root.attributes('-alpha', 0.0)  # Set transparency level (80% opacity)

# Optionally, make the window frameless
root.overrideredirect(True)  # Removes the window frame and title bar

# Define window size
window_width = 400
window_height = 150

# Calculate the x and y coordinates to position the window at the bottom-right corner
x = screen_width - window_width - 0  # 10px padding from right
y = screen_height - window_height - 0  # 50px padding from bottom (adjust for taskbar)






window = webview.create_window('Pop-up Window', 'popup.html', width=window_width, height=window_height, x=x, y=y, frameless=True)

# Start the webview window
webview.start()
