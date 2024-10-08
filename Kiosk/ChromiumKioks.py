import os
from time import sleep
import webbrowser

def search():

  #new browser object
 chrome = webbrowser.get('chromium-browser')
  #search engine startpoint
 google = chrome.open_new("https://www.google.com")

if __name__ == "__main__":
 sleep(0.5)
 search()
 sleep(1)