import bs4
import requests

res = requests.get("https://www.flipkart.com/adidas-adiray-m-running-shoes-men/p/itmf7g8fxnxydsuc?pid=SHOF7G8FQHSYNKHZ&lid=LSTSHOF7G8FQHSYNKHZBV5ME8&marketplace=FLIPKART&sattr[]=size&st=size")

soup = bs4.BeautifulSoup(res.text, "lxml")

discount = soup.select(".VGWI6T _1iCvwn _9Z7kX3")

originalPrice = soup.select("._3auQ3N _1POkHg")

numberOfReviews = soup.select("._38sUEc")

deliveryTime = soup.select("._29Zp1s")

rating = soup.select(".hGSR34 bqXGTW")


print(discount[0].getText())
print(originalPrice[0].getText())
print(numberOfReviews[0].getText())
print(deliveryTime[0].getText())
print(rating[0].getText())
