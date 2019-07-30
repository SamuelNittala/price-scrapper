from telegram.ext import *
from scrap import url
from scrap import scrap
from bs4 import BeautifulSoup
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token=' TOKEN ')

dispatcher = updater.dispatcher
url_box = []

def show(bot,update):
        query = update.message.text[5:]
        contents = url.add_url(query)
        update.message.reply_text('Choose the product to add')
        for i,c in enumerate(contents):
                update.message.reply_text("%d %s"%(i+1,c.get_text()))
        
def add(bot,update):
        get_choice = update.message.text.split(',')
        query = get_choice[0][3:]
        choice = int(get_choice[1])
        contents = url.add_url(query)
        price = scrap.get_price('https://www.amazon.in'+contents[choice-1].parent['href'])
        update.message.reply_text("Current price of %s is %s"%(contents[choice-1].get_text(),price))

        

def get_input(bot,update):
        return update

add_handler = CommandHandler('add',add)
show_handler = CommandHandler('show',show)
msg_handler = MessageHandler(Filters.text,get_input)

dispatcher.add_handler(msg_handler)
dispatcher.add_handler(show_handler)
dispatcher.add_handler(add_handler)

updater.start_polling()