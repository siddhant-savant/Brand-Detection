import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://www.boots.com/dior-miss-dior-eau-de-parfum-50ml-10300555').text
soup = BeautifulSoup(html_text, "lxml")

product_name = soup.find('h1').text
product_price = soup.find('div', class_ = 'price price_redesign').text
product_brand = soup.find('input', { 'id': 'productManufacturerName'})['value']
#product_sku_id = soup.find('input', { 'id': 'dlProductId_2590187'})['value'].replace('.P', '')

stock_status = soup.find('div', class_ = 'productDetailsQuanAndActContainer')
product_stock_sts = stock_status.find('div', class_ = 'button_text').text.strip()

print(f'''
    Product Brand  :{product_brand}
    Product Name   :{product_name}
    Product Price  :{product_price}
    Stock Status   :{product_stock_sts}
    ''')
