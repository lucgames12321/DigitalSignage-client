import tkinter as tk
from tkinter import messagebox
import os

# Ensure this is set correctly!!!!!!
os.environ["DISPLAY"] = ":0"   

def create_notification_bar(notification_message):
    # Create a root window (but we'll hide it, it's just needed for initialization)
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    
    # Create a Toplevel window that will act as the notification bar
    notification_bar = tk.Toplevel(root)
    
    # Remove window decorations (e.g., close, minimize buttons)
    notification_bar.overrideredirect(True)
    
    # Set the window always on top
    notification_bar.attributes("-topmost", True)
    
    # Set the background color
    notification_bar.configure(bg="#fd7e14")
    
    # Create a label to display the notification message
    notification_label = tk.Label(
        notification_bar, 
        text=notification_message, 
        bg="#fd7e14", 
        fg="#f8f9fa", 
        font=("Comic Sans MS", 24, "bold"),
        wraplength=notification_bar.winfo_screenwidth() - 20  # Set wrap length to screen width with padding
    )
    
    # Center the label in the notification bar
    notification_label.pack(expand=True, padx=10, pady=5)
    
    # Set the position and size of the notification bar
    screen_width = notification_bar.winfo_screenwidth()
    notification_bar.geometry(f"{screen_width}x80+0+0")  # Full width, 80px height, positioned at the top

# Initialize notification_bar variable
notification_bar = None

while True:
    # Prompt the user for a URL
    print("Geef een notificatie melding op of type 'exit' om de meldingen af te sluiten:")
    notificatie = input()

    # Exit condition
    if notificatie.lower() == 'exit':
        if notification_bar is not None:
            notification_bar.destroy()
        print("Exiting the script and closing the melding.")
        break

    else:
        print("printing melding:", notificatie)
        notification_bar = create_notification_bar(notificatie)
