from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import pandas as pd
from datetime import datetime

current_date = datetime.now().date()
date = current_date.strftime('%Y-%m-%d')

os.environ['PATH'] += r"C:/Users/siddh/Desktop/Dissertation/Scripts"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()


url = 'https://www.notino.co.uk/womens-perfume/'
driver.get(url)
time.sleep(3)

black_friday_popup = driver.find_element(By.CLASS_NAME,'exponea-close-cross').click()
time.sleep(3)

y = 1000
for timer in range(0,8):
     driver.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 1000  
     time.sleep(0.6)
     print('scrolling to the footer..')

print('reached page footer')
     
driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
time.sleep(5)

# pl_grid = driver.find_element(By.ID,'productListWrapper')
#styled__ProductListingWrapper-sc-fqtc0u-6 kJidVJ
#styled__PageGridWrapper-sc-1yds6ou-0 boEKwk
#styled__Wrapper-sc-1aw2wjn-0 kCrWYx
pl_grid = driver.find_elements(By.CSS_SELECTOR, '[data-testid="product-container"]')
for container in pl_grid:
    # Extract product name, brand, and price
    product_name = container.find_element(By.CSS_SELECTOR, 'h2').text
    brand = container.find_element(By.CSS_SELECTOR, 'h3').text
    price = container.find_element(By.CSS_SELECTOR, '[data-testid="price-component"]').text

    # Print or store the extracted information
    print(f"Product Name: {product_name}")
    print(f"Brand: {brand}")
    print(f"Price: {price}")
    print("\n")

# Close the webdriver
driver.quit()