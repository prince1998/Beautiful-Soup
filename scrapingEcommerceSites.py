import bs4
import requests

res = requests.get("https://www.koovs.com/men/footwear/?type=list&sort=relevance&filter_brand_fq=253")

soup = bs4.BeautifulSoup(res.text, "lxml")

priceKoovs = soup.select(".product_price")


print(priceKoovs[0].getText()) #works

res = requests.get("https://www.jabong.com/men-sports-shoes")

soup = bs4.BeautifulSoup(res.text, "lxml")

priceJabong = soup.select(".standard-price")


print(priceJabong[0].getText()) #works



res = requests.get("http://yepme.com/men/footwear/sports-shoes/29/288")

soup = bs4.BeautifulSoup(res.text, "lxml")

print(rsoup)
print(priceYepme[0].getText()) #doesnt work

#Ajio, yepme doesnt work
#koovs very limited shoes  adidas - 17 nike 72
#fashos no  nike and adidas no point
