import bs4 as bs
from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.parse import urlparse
from nltk.tokenize import sent_tokenize, word_tokenize
import operator

source = urllib.request.urlopen('http://archives.eenadu.net/10-21-2018/home.aspx').read()
soup = bs.BeautifulSoup(source,'lxml')

for link in soup.select("a[href$='.aspx']"):
	url2 = link.get('href')	
	result = urlparse(url2)
	
	if all([result.scheme, result.netloc]):
		filename = 'ph_ftrs51_telugu.txt'
		r = requests.get(url2)
		type(r)
		
		html = r.text
		soup = BeautifulSoup(html, "html5lib")
		type(soup)
		text = soup.get_text()	
		words = word_tokenize(text)
		
		phword = []
		file = open(filename)
		for line in file:
			phword.append(line.strip())
			
		word_freq = []
		
		for s in phword:
			n = operator.countOf(words, s)
			if n > 0:
				word_freq.append([s])
				word_freq.append([n])
		
		print(url2,'	frequency=	',word_freq)
		