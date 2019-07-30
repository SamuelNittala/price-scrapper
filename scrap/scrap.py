import requests
from bs4 import BeautifulSoup
from header import headers

def get_price(url):
    page = requests.get(url,headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        price = soup.find(id='priceblock_ourprice').get_text()
    except:
        price = soup.find(id='priceblock_dealprice').get_text()

    '''comma = price.find(',') 
    dot = price.find('.')

    float_price = (float) (price[2:comma] + price[comma+1:])'''

    return price




