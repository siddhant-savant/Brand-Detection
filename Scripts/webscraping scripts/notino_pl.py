import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

current_date = datetime.now().date()
date = current_date.strftime('%Y-%m-%d')

url = 'https://www.notino.co.uk/womens-perfume/'

pl_page = []
position = 1

response = requests.get(url).text
soup = BeautifulSoup(response, "lxml")

pl_grid = soup.find('div', class_ ='styled__PageGridWrapper-sc-1yds6ou-0 boEKwk')
pl_products = pl_grid.find_all('div', class_ = 'sc-brPLxw sc-jGKxIK hgWOPy gYhoGI styled__StyledProductTile-sc-1i2ozu3-0 cGncNV')

for products in pl_products:
    product_brand = products.find('h2').text     #~~~Brand 
    product_name = products.find('h3').text
    product_type = products.find('p').text
    
    product_concat_name = product_name+' '+product_type      #~~~Name
    
    product_pp = products.find('div', class_ = 'sc-bbSZdi gEHAOh').text.replace('£','')
    product_price = product_pp.replace('from','').strip()        #~~~Price
    
    pdp_url = products.find('a')['href']
    pdp_url_concat = 'https://www.notino.co.uk'+pdp_url  #~~~ PDP Urls
    
    product_category = 'Fragrance'               #~~~Category
    product_subcategory = 'Womens Fragrance'     #~~~Subcategory
    retailer = 'Notino'                          #~~~Retailer
    sponsored = 'N/A'
    sku_id = 'N/A'
    
    pl_page.append([position,product_brand,product_concat_name,pdp_url_concat,product_price,sku_id,date,sponsored,product_category,product_subcategory,retailer,url])
    position = position+1
    
file = pd.DataFrame(pl_page, columns=['Position','Brand','Product_Name','Product_Page_Url','Price','Product_SKU_ID','Date','Sponsored','Product_Category','Product_Subcategory','Retailer','Input_Url'])
file.to_csv('Notino_PL_Output_'+date+'.csv', index=False)

print('file created')
    
    
    