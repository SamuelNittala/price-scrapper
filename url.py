from bs4 import BeautifulSoup
import requests
from header import headers

url_arr = []

def add_url(search_text):
    search_text = search_text.replace(' ','+')
    search_page = requests.get('https://www.amazon.in/s?k='+search_text,headers=headers)
    soup = BeautifulSoup(search_page.content,'html.parser')
    contents = soup.find_all(class_ ='a-size-medium',limit = 4)
    for c in contents:
        c_text = c.get_text()
        print(c_text)
        if(c_text.find(search_text) != -1):
            print(c.parent['href'])

add_url('Iphone X')
