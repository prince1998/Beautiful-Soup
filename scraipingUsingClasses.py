#Program to scrape classes and tags.
#'The Band' : <h3>THE BAND</h3>
#'Contact' : <h3 class="text-center">Contact</h3>

import bs4
import requests

res = requests.get('https://prince1998.github.io');
soup = bs4.BeautifulSoup(res.text,'lxml')
h3 = soup.select('h3')

print(h3[0].getText()) #prints 'The Band'
print(h3[1].getText()) #prints 'Contact'

contact = soup.select('h3.text-center')

print(contact[0].getText()) #prints contact

res = requests.get('https://en.wikipedia.org/wiki/Macro_(computer_science)#Assembly_language')
soup = bs4.BeautifulSoup(res.text,'lxml')
heading = soup.select('.mw-headline')
print(heading)

for i in heading:
    print(i.getText())
    
contents = soup.select('.toctext')
print(contents)

for i in contents:
    print(i.getText())
    
    


