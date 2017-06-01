import telegram.ext as t
import requests
from bs4 import BeautifulSoup
import datetime

def futures(bot, update):
    mylist=[]
    res = requests.get('http://www.etnet.com.hk/www/eng/futures/index.php')
    soup = BeautifulSoup(res.text, "lxml")
    m = 0
    for n in soup.select('{}'.format('.FuturesQuoteName')):
        mylist.append(n.get_text())
    for n in soup.select('{}'.format('.FuturesQuoteNominal')):
        mylist.append(n.get_text())
    for n in soup.select('{}'.format('.FuturesQuoteOthers')):
        mylist.append(n.get_text())
    for n in soup.select('{}'.format('.FuturesQuoteNominal2')):
        mylist.append(n.get_text())
    mylist = [i.replace('\xa0\xa0',"").replace('\u3000',"").replace("C\u00ef\u00b8\u00b0", "Pre Close : ").replace("\u00e3\u0080\u0080\u00e3\u0080\u0080O\u00ef\u00b8\u00b0", "                            Open : ").replace("\u00e3\u0080\u0080\u00e3\u0080\u0080H / L\u00ef\u00b8\u00b0", "                                     High / Low : ") for i in mylist]
    del mylist[6]
    mylist.insert(1, mylist.pop(3))
    mylist.insert(3, mylist.pop(4))
    mylist.insert(2, mylist.pop(5))
    mylist.insert(5, mylist.pop(6))
    mylist.insert(7, mylist.pop(8))
    text = 'Regular Market: ' + mylist[1] + '\n' + 'ATH Market: ' + mylist[4] + '\n' + 'Time: ' + str(datetime.datetime.now().strftime('%H:%M:%S'))
    update.message.reply_text(text)

updater = t.Updater('328196434:AAE87OJ1-QvqGbAyOGKorlWgThB3XziJXKA')

updater.dispatcher.add_handler(t.CommandHandler('futures', futures))

updater.start_polling()
updater.idle()
