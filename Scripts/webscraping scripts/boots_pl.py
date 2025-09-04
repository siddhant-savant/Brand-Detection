import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

current_date = datetime.now().date()
date = current_date.strftime('%Y-%m-%d')

url = 'https://www.boots.com/fragrance/perfume/all-perfume'

response = requests.get(url)
response = response.content
soup = BeautifulSoup(response, 'html.parser')

pl_grid = soup.find('div', class_ ='product_listing_container')
pl_products_grid = pl_grid.find_all('div', class_ = 'estore_product_container')

pl_page = []
position = 1

for products in pl_products_grid:
    prod_top = products.find('div', class_ = 'product_top_section')
    top_name = prod_top.find('div', class_ = 'product_name')
    product_name = top_name.find('a', class_ = 'product_name_link product_view_gtm').text
    
    prod_rr = products.find('div', class_ = 'product_rating')
    product_ratings = prod_rr.find('span')
    stars = product_ratings.attrs['alt']
    stars = stars.split()[0]
    product_reviews = prod_rr.find('a', class_ = 'product_review_count').text.replace('(','')
    product_reviews = product_reviews.replace(')','')
    
    prod_info = products.find('div', class_ = 'product_info')
    product_price = prod_info.find('div', class_ = 'product_price').text.strip().replace('£','')
    
    prod_sku_id = products.attrs['data-productid']
    prod_sku_id = prod_sku_id.replace('.P', '')
    
    pl_page.append([position,product_name,stars,product_reviews, product_price, prod_sku_id, date])
    position = position + 1

df = pd.DataFrame(pl_page, columns= ['Position', 'Product_Name','Rating','Reviews','Price','Prod_SKU_ID', 'Date'])
df.to_csv('Boots_PL_Output.csv', index=False)