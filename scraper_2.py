import sys
import requests
import bs4


#Its will go to the url and take whatever is inside the perticular tag
search='Scrape'
res=requests.get('https://en.wikipedia.org/wiki/'+search)
wiki=bs4.BeautifulSoup(res.text,"html.parser")
for i in wiki.select("div"):
	print(i.getText())