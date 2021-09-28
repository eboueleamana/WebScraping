#pip install beautifulsoup4
#pip install requests

import requests
from bs4 import BeautifulSoup
import pandas as pd

url="http://feeds.bbci.co.uk/news/rss.xml"

#import le code de la page
reponse=requests.get(url)
soup = BeautifulSoup(reponse.text,"html.parser")

items = soup.findAll('item')

#item=items[0]
#item.description.text

news_items=[]

for i in items:
  news_i={}
  news_i['title']= i.title.text
  news_i['description']= i.description.text
  news_i['pubdate']= i.pubdate.text
  news_items.append(news_i)


news_items

#Convertir la liste en base de donnés
df=pd.DataFrame(news_items,columns=['title','description','pubdate'])
df.head

#Générer le fichier CSV

df.to_csv('web_scraping.csv', index=False, encoding='utf-8')