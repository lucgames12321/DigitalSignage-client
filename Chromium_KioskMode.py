 from selenium import webdriver
 from selenium.webdriver.support import ui
 from selenium.webdriver.chrome.options import Options

 option = Options()
 option.add_argument("--start-maximized")
 option.add_argument("--no-sandbox")
 option.add_argument("--disable-web-security")
 option.add_argument("--ignore-certificate-errors")
 option.add_argument("--kiosk")
 option.add_argument("--disable-password-manager-reauthentication")

driver = webdriver.Chrome("C:/chromedriver.exe",0,option)