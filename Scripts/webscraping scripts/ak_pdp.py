import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

current_date = datetime.now().date()
date = current_date.strftime('%Y-%m-%d')

urls = ['https://www.boots.com/lancome-monsieur-big-mascara-10248818',
        'https://www.boots.com/too-faced-better-than-sex-mascara-black-8ml-10263216']

pdp_op = []

def webscrape(url):
    
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")
    
    product_name = soup.find('h1').text
    #size = product_name.split(' ')[-1]
    
    size = ' '.join(soup.find('div', class_='details details_redesign').text.split(' ')[0:2])
    
    product_price = soup.find('div', class_ = 'price price_redesign').text.strip().replace('£','')
    product_brand = soup.find('input', { 'id': 'productManufacturerName'})['value']
    
    stock_status = soup.find('div', class_ = 'productDetailsQuanAndActContainer')
    product_stock_sts = stock_status.find('div', class_ = 'button_text').text.strip()
    if 'Add to basket' in product_stock_sts:
        stock_status_v1 = 'In Stock'
    else:
        stock_status_v1 = 'Out of Stock'
    
    sku_id = url.split('-')[-1]
    
    if 'lancome' in url:
      brand_status = 'Lancome'
    else:
        brand_status = 'Competitor'
    
    product_cat = 'Fragrance'
    product_subcat = 'Womens Fragrance'
    retailer = 'Boots'
    
    reviews = 0
    ratings = 0
    url = url
    
    pdp_op.append([product_cat,product_subcat,product_brand,product_name,product_price,size,stock_status_v1,product_stock_sts,sku_id,ratings,reviews,brand_status, date,retailer,url])
        
    df = pd.DataFrame(pdp_op, columns= ['Product_Category','Product_Subcategory','Product_Brand','Product_Name','Product_Price','Size','Stock_Status','Product_Availability','Sku_Id','Rating','Reviews','Brand_Status', 'Date','Retailer','url'])
    df.to_csv('Boots_PDP_Output_'+date+'.csv', index=False)

for url in urls:
    webscrape(url)
    print('sku appended..')

print('file created')