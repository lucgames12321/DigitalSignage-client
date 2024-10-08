import tkinter as tk
from tkinter import messagebox

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
    
    # Set the background color and the message
    notification_bar.configure(bg="yellow")
    
    # Create a label to display the notification message
    notification_label = tk.Label(
        notification_bar, 
        text=notification_message, 
        bg="yellow", 
        fg="black", 
        font=("Helvetica", 12)
    )
    notification_label.pack(padx=10, pady=5)
    
    # Set the position and size of the notification bar
    screen_width = notification_bar.winfo_screenwidth()
    notification_bar.geometry(f"{screen_width}x30+0+0")  # Full width, 30px height, positioned at the top
    
    # Destroy the notification after 5 seconds
    notification_bar.after(5000, notification_bar.destroy)

    # Run the Tkinter main loop
    root.mainloop()
    exit()


# Usage example:
if __name__ == "__main__":
    create_notification_bar("This is a notification!")
