import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

current_date = datetime.now().date()
date = current_date.strftime('%Y-%m-%d')

url = 'https://www.boots.com/fragrance/perfume/all-perfume'

pl_page = []
position = 1

response = requests.get(url)
response = response.content
soup = BeautifulSoup(response, 'html.parser')

pl_grid = soup.find('div', class_ ='product_listing_container')
product_list = pl_grid.find_all('li')

for products in product_list:
    product_attrs = products.find('div', class_ = 'product_top_section')
    product_name = product_attrs.find('a')['aria-label'] ##
    brand = 'brand'

    pdp_url = product_attrs.find('a')['href']            ##

    prod_price = product_attrs.find('a')['data-value']
    price = json.loads(prod_price)['price']              ##

    sku_id = pdp_url.split('-')[-1]                      ##
  
    sponsored = 'N/A'                                    ##
    prod_cat = 'Fragrance'                               ##
    prod_subcat = 'Womens Fragrance'                     ##
    retailer = 'Boots'                                   ##
    ip_url = url                                         ##
    pl_page.append([position,brand,product_name,pdp_url,price,sku_id,date,sponsored,prod_cat,prod_subcat,retailer,ip_url])
    position = position+1

file = pd.DataFrame(pl_page, columns=['Position','Brand','Product_Name','Product_Page_Url','Price','Product_SKU_ID','Date','Sponsored','Product_Category','Product_Subcategory','Retailer','Input_Url'])
file.to_csv('Boots_PL_Output_'+date+'.csv', index=False)

print('file created')