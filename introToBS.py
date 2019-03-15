#Program to scrape title of my website.

import bs4
import requests

res = requests.get('https://prince1998.github.io'); #makes a request to webpage
#res.text will display source code of webpage

#type(res) displays res type as request 

soup = bs4.BeautifulSoup(res.text,'lxml') #converting res from object of type request to object of type BeautifulSoup and structuring it by lxml parser

#type(soup) displays soup type as BeautifulSoup

title = soup.select('title') 
print(title[0].getText()) 
