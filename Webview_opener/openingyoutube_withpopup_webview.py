import webview

if __name__ == '__main__':
    webview.create_window('Youtube Player', 'youtube_player.html', transparent=True, frameless=True, fullscreen=True)
    # Create a transparent webview window
    webview.create_window('Popup melding', 'popup.html', transparent=True, frameless=True)
    webview.start()
