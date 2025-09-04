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
for timer in range(0,7):
     driver.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 1000  
     time.sleep(0.6)
     print('scrolling to the footer..')

print('reached page footer')
     
driver.execute_script("window.scrollTo(0, document.body.scrollTop);")
time.sleep(5)

position = 1
pl_page = []

product_elements = driver.find_elements(By.CLASS_NAME, 'styled__PageGridWrapper-sc-1yds6ou-0') #styled__StyledProductTile-sc-1i2ozu3-0

# for product in pl_grid:
     # brand_element = product.find_element(By.TAG_NAME, 'h2').text.strip()
     # print(brand_element)

     # position =position+1
     # # print(product.text)




# for product in pl_grid:
#     brand_element = product.find_element(By.CLASS_NAME, 'h2.sc-gEvEer.sc-iMTnTL.pWgxV.diVDhy').text
#     product_name_element = product.find_element(By.CLASS_NAME, 'h3.sc-krNlru.dbGhzH.hIrAJY').text
#     perfume_type = product.find_element(By.CLASS_NAME, 'sc-jaXxmE.lmGZrN').text
#     product_name = product_name_element +' '+ perfume_type
#     price_element = product.find_element(By.CSS_SELECTOR, 'div.sc-bbSZdi.gEHAOh').text.replace('from','').replace('\n', '').replace('£', '')
#     sponsored_tag = product.find_elements(By.CLASS_NAME, 'styled__StyledSponsoredLabel-sc-1nyfhnp-0')
#     #pdp_url = product.find_element(By.CSS_SELECTOR, 'a').get_attribute('href').text
#     pdp_url_concat = product.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    
#     product_category = 'Fragrance'               #~~~Category
#     product_subcategory = 'Womens Fragrance'     #~~~Subcategory
#     retailer = 'Notino'                          #~~~Retailer
#     sponsored = 'N/A'
#     sku_id = 'N/A'
#     Sponsored = "Sponsored" if sponsored_tag else "N/A"
    
#     pl_page.append([position,brand_element,product_name,pdp_url_concat,price_element,sku_id,date,Sponsored,product_category,product_subcategory,retailer,url])
#     position =position+1
    
    
# file = pd.DataFrame(pl_page, columns=['Position','Brand','Product_Name','Product_Page_Url','Price','Product_SKU_ID','Date','Sponsored','Product_Category','Product_Subcategory','Retailer','Input_Url'])
# file.to_csv('Notino_PL_Output_'+date+'.csv', index=False)
product_containers = driver.find_elements(By.CSS_SELECTOR, 'div.styled__StyledProductTile-sc-1i2ozu3-0')

for position, product_container in enumerate(product_containers, start=1):
    brand = product_container.find_element(By.TAG_NAME, 'h2').text.strip()
    product_name = product_container.find_element(By.TAG_NAME, 'h3').text.strip()
    price_element = product_container.find_element(By.CSS_SELECTOR, 'span.sc-kOPcWz')  # Assuming this class contains the price
    price = float(price_element.text.strip()) if price_element else None

    pl_page.append({
        'position': position,
        'brand': brand,
        'product_name': product_name,
        'price': price
    })

# Sort the list of dictionaries by position, brand, product name, and price
sorted_data = sorted(pl_page, key=lambda x: (x['position'], x['brand'], x['product_name'], x['price']))

# Print the sorted data
for item in sorted_data:
    print(f"Position: {item['position']}, Brand: {item['brand']}, Product Name: {item['product_name']}, Price: £{item['price']:.2f}")
