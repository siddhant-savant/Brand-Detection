import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

current_date = datetime.now().date()
date = current_date.strftime('%Y-%m-%d')

urls = ['https://www.notino.co.uk/dior/miss-dior-eau-de-parfum-for-women/p-16086004/',
        'https://www.notino.co.uk/yves-saint-laurent/black-opium-eau-de-parfum-for-women/p-451793/',
        'https://www.notino.co.uk/armani/my-way-floral-eau-de-parfum-refillable-for-women/p-16125478/',
        'https://www.notino.co.uk/lancome/la-vie-est-belle-intensement-eau-de-parfum-for-women/p-16014084/',
        'https://www.notino.co.uk/prada/prada-paradoxe-eau-de-parfum-refillable-for-women/p-16143146/']

pdp_op = []

def webscrape(url):
    
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")

    product_name = soup.find('span', class_ = 'sc-3sotvb-4 kSRNEJ').text
    product_type = soup.find('span', class_ = 'sc-3sotvb-5 bBQCfG').text

    product_brand = soup.find('a', class_ = 'sc-3sotvb-2 iYvTNX').text

    product_namecat = (product_brand+' '+product_name+product_type)

    product_size = soup.find('div', class_ = 'sc-h83s98-4 fqSniA').text
    product_ss = soup.find('div', class_ = 'sc-mu8uqe-0 fKkBSf').text.split('|')[0]
    if 'currently unavailable' in product_ss:
        prod_stock = 'Out of Stock'
        product_price = 'N/A'
        
    else:
        prod_stock = 'In Stock'
        product_price = soup.find('div', class_ = 'sc-mirfw-1 isJYDN').text.strip().replace('£','')
        
    sku_id = url.split('-')[-1].replace('/', '')

    if 'dior' in url:
        brand_status = 'Dior'
    else:
        brand_status = 'Competitor'
            
    product_cat = 'Fragrance'
    product_subcat = 'Womens Fragrance'
    retailer = 'Notino'
    
    pdp_op.append([product_cat,product_subcat,product_brand,product_namecat,product_price,product_size,prod_stock,product_ss,sku_id,brand_status,date,retailer])
    df = pd.DataFrame(pdp_op, columns= ['Product_Category','Product_Subcategory','Product_Brand','Product_Name','Product_Price','Size','Stock_Status','Product_Availability','Sku_Id','Brand_Status', 'Date','Retailer'])
    df.to_csv('Notino_PDP_Output_'+date+'.csv', index=False)
    
for url in urls:
    webscrape(url)
    print('sku appended..')

print('file created')
    
    