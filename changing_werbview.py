import time

import webview

def change_url(window):
    # wait a few seconds before changing url:
    time.sleep(2)

    # change url:
    window.load_url('https://pywebview.flowrl.com/hello')

if __name__ == '__main__':
    window = webview.create_window('URL Change Example', 'http://www.google.com', fullscreen=True)
    webview.start(change_url, window)
