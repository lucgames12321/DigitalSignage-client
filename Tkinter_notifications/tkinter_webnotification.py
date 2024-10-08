import tkinter as tk
import webview  # pywebview to render HTML

# Function to create the notification bar using pywebview inside tkinter
def create_notification_bar():
    root = tk.Tk()
    root.title("HTML Notification Bar")

    # Set window size to the width of the screen and a small height (e.g., 50px)
    screen_width = root.winfo_screenwidth()
    bar_height = 100  # You can adjust the height
    root.geometry(f"{screen_width}x{bar_height}+0+0")  # Full width, top of the screen

    # Make the window borderless
    root.overrideredirect(True)

    # Create a pywebview window within tkinter
    webview.create_window("Notification", "notification.html", frameless=True, width=screen_width, height=bar_height)

    # Start the webview (this will run the webview loop)
    webview.start()

    # Close the tkinter window after the webview is done
    root.mainloop()

# Example usage
if __name__ == "__main__":
    create_notification_bar()
