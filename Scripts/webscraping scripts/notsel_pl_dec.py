import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

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

y = 1000
for timer in range(0, 7):
    driver.execute_script("window.scrollTo(0, "+str(y)+")")
    y += 1000
    time.sleep(0.6)
    print('scrolling to the footer..')

print('reached page footer')

driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
time.sleep(5)

position = 1
pl_page = []

product_containers = driver.find_elements(By.CSS_SELECTOR, 'div.styled__StyledProductTile-sc-1i2ozu3-0')

for position, product_container in enumerate(product_containers, start=1):
    brand = product_container.find_element(By.TAG_NAME, 'h2').text.strip()
    product_name = product_container.find_element(By.TAG_NAME, 'h3').text.strip()
    price_element = product_container.find_element(By.CSS_SELECTOR, 'span.sc-kOPcWz')
    price = float(price_element.text.strip()) if price_element else None

    sponsored_tag = product_container.find_elements(By.CLASS_NAME, 'styled__StyledSponsoredLabel-sc-1nyfhnp-0')
    sponsored = "Sponsored" if sponsored_tag else "N/A"
    sku_id = 'N/A'
    
    pdp_url_concat = product_container.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    
    product_category = 'Fragrance'  # ~~~Category
    product_subcategory = 'Womens Fragrance'  # ~~~Subcategory
    retailer = 'Notino'  # ~~~Retailer

    pl_page.append([position, brand, product_name, pdp_url_concat, price, sku_id, date, sponsored,
                    product_category, product_subcategory, retailer, url])
    position = position + 1

file = pd.DataFrame(pl_page, columns=['Position', 'Brand', 'Product_Name', 'Product_Page_Url', 'Price', 'Product_SKU_ID','Date', 'Sponsored', 'Product_Category', 'Product_Subcategory', 'Retailer', 'Input_Url'])
file.to_csv('Notino_PL_Output_'+date+'.csv', index=False)
print('file created')


driver.quit()
