import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

current_date = datetime.now().date()
date = current_date.strftime('%Y-%m-%d')

urls = ['https://www.boots.com/dior-miss-dior-eau-de-parfum-50ml-10300555',
        'https://www.boots.com/yves-saint-laurent-black-opium-eau-de-parfum-50ml-10180311',
        'https://www.boots.com/armani-my-way-floral-eau-de-parfum-50ml-10314493',
        'https://www.boots.com/lancome-la-vie-est-belle-eau-de-parfum-50ml-10145849',
        'https://www.boots.com/prada-paradoxe-eau-de-parfum-50ml-10317217']

pdp_op = []

for url in urls:
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")
    
    product_name = soup.find('h1').text
    size = product_name.split(' ')[-1]
    
    product_price = soup.find('div', class_ = 'price price_redesign').text.strip().replace('£','')
    product_brand = soup.find('input', { 'id': 'productManufacturerName'})['value']
    
    stock_status = soup.find('div', class_ = 'productDetailsQuanAndActContainer') 
    product_stock_sts = stock_status.find('div', class_ = 'button_text').text.strip()
    if 'Add to basket' in product_stock_sts:
        stock_status_v1 = 'In Stock'
    else:
        stock_status_v1 = 'Out of Stock'
    
    sku_id = url.split('-')[-1]
    
    if 'dior' in url:
      brand_status = 'Dior'
    else:
        brand_status = 'Competitor'
    
    product_cat = 'Fragrance'
    product_subcat = 'Womens Fragrance'
    retailer = 'Boots'
    
    # print(f'''
    #     Product Brand  :{product_brand}
    #     Product Name   :{product_name}
    #     Product Price  :{product_price}
    #     Stock Status   :{product_stock_sts}
    #     ''')
    
    pdp_op.append([product_cat,product_subcat,product_brand,product_name,product_price,size,stock_status_v1,product_stock_sts,sku_id,brand_status, date,retailer]) 
    
df = pd.DataFrame(pdp_op, columns= ['Product_Category','Product_Subcategory','Product_Brand','Product_Name','Product_Price','Size','Stock_Status','Product_Availability','Sku_Id','Brand_Status', 'Date','Retailer'])
df.to_csv('Boots_PDP_Output_'+date+'.csv', index=False)