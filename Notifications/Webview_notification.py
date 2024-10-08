import tkinter as tk
from tkinter import simpledialog
from tkhtmlview import HTMLLabel

def create_notification_bar(notification_message):
    # Create a new Toplevel window for the notification bar
    notification_bar = tk.Toplevel(root)

    # Remove window decorations (e.g., close, minimize buttons)
    notification_bar.overrideredirect(True)

    # Set the window always on top
    notification_bar.attributes("-topmost", True)

    # Set the size of the notification bar
    screen_width = notification_bar.winfo_screenwidth()
    notification_bar.geometry(f"{screen_width}x100+0+0")  # Full width, 100px height, positioned at the top

    # Create an HTMLLabel to display the notification message
    html_content = f"""
    <div style="background-color: #ffcc00; color: black; font-family: Arial; font-size: 24px; text-align: center; padding: 20px;">
        {notification_message}
    </div>
    """
    
    # Create an HTMLLabel and pack it into the notification bar
    html_label = HTMLLabel(notification_bar, html=html_content)
    html_label.pack(fill=tk.BOTH, expand=True)

    # Close the notification bar after 5 seconds
    notification_bar.after(5000, notification_bar.destroy)

def notification_loop():
    while True:
        # Prompt the user for a notification message
        notification_message = simpledialog.askstring("Notification", "Enter a notification message (type 'exit' to quit):")

        # Exit condition
        if notification_message is None or notification_message.lower() == 'exit':
            print("Exiting the script and closing the notifications.")
            break
        else:
            print("Displaying notification:", notification_message)
            create_notification_bar(notification_message)

# Create the main Tkinter window (it will be hidden)
root = tk.Tk()
root.withdraw()  # Hide the main window

# Start the notification loop
notification_loop()
