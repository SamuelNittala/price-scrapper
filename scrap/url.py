from bs4 import BeautifulSoup
import requests
from header import headers

def add_url(url_arr,search_text):
    tmp = search_text
    search_text = search_text.replace(' ','+')
    search_page = requests.get('https://www.amazon.in/s?k='+search_text,headers=headers)
    soup = BeautifulSoup(search_page.content,'html.parser')

    contents = soup.find_all(class_ ='a-size-medium',limit = 4)
    
    print('Choose the product you wish to add\n')
    for i,c in enumerate(contents[1:]):
        c_text = c.get_text()
        print("%d:%s\n"%(i+1,c_text))
    i = input('Enter id: ')
    url_arr.append('https://www.amazon.in'+contents[i].parent['href'])