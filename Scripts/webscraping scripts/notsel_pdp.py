from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
from datetime import datetime

current_date = datetime.now().date()
date = current_date.strftime('%Y-%m-%d')

pdp_op = []

urls = ['https://www.notino.co.uk/dior/miss-dior-eau-de-parfum-for-women/p-16086004/',
        'https://www.notino.co.uk/yves-saint-laurent/black-opium-eau-de-parfum-for-women/p-451793/',
        'https://www.notino.co.uk/armani/my-way-floral-eau-de-parfum-refillable-for-women/p-16125478/',
        'https://www.notino.co.uk/lancome/la-vie-est-belle-intensement-eau-de-parfum-for-women/p-16014084/',
        'https://www.notino.co.uk/prada/prada-paradoxe-eau-de-parfum-refillable-for-women/p-16143146/']


for url in urls:
        os.environ['PATH'] += r"C:/Users/siddh/Desktop/Dissertation/Scripts"

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
        
        driver.get(url)
        time.sleep(3)

        brand_element = driver.find_element(By.CSS_SELECTOR, 'a.sc-3sotvb-2')
        brand = brand_element.text

        product_name_element = driver.find_element(By.CSS_SELECTOR, 'span.sc-3sotvb-4')
        product_name = product_name_element.text

        description_element = driver.find_element(By.CSS_SELECTOR, 'span.sc-3sotvb-5')
        description = description_element.text
        product_concat_name = product_name +' '+ description

        quantity_element = driver.find_element(By.CSS_SELECTOR, 'div.sc-h83s98-4')
        quantity = quantity_element.text
        
        try:
                price_element = driver.find_element(By.ID, 'pd-price')
                price = price_element.text.replace('£', '')
        
        except NoSuchElementException:
                print("Price not available")
                price = 'n/a'

        availability_element = driver.find_element(By.CSS_SELECTOR, 'span.sc-mu8uqe-4')
        availability = availability_element.text
        
        driver.quit()
        
        prod_ss = availability
        sku_id = url.split('-')[-1].replace('/', '')

        if 'dior' in url:
                brand_status = 'Dior'
        else:
                brand_status = 'Competitor'

        product_cat = 'Fragrance'
        product_subcat = 'Womens Fragrance'
        retailer = 'Notino'
        
        pdp_op.append([product_cat,product_subcat,brand,product_concat_name,price,quantity,availability,prod_ss,sku_id,brand_status,date,retailer])
        df = pd.DataFrame(pdp_op, columns= ['Product_Category','Product_Subcategory','Product_Brand','Product_Name','Product_Price','Size','Stock_Status','Product_Availability','Sku_Id','Brand_Status', 'Date','Retailer'])
        print('sku appended..')


df.to_csv('Notino_PDP_Output_'+date+'.csv', index=False)
print('file created')