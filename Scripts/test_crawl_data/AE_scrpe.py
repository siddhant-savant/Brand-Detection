import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


os.environ['PATH'] += r"C:/Users/siddh/Desktop/Dissertation/Scripts"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.co.uk/')

# driver_path = "C:/Users/siddh/Desktop/Dissertation/Scripts/chromedriver.exe"
# chr_options = Options()
# chr_options.add_experimental_option("detach", True)
# chr_driver = webdriver.Chrome(options=chr_options)
# chr_driver.get("https://www.google.co.uk/")
# time.sleep(5000)