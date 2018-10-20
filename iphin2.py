import nltk
import requests
import bs4
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
from collections import Counter
import operator

url1 = 'https://timesofindia.indiatimes.com/2018/10/18/archivelist/year-2018,month-10,starttime-43391.cms'

html = requests.get(url1)
soup = bs4.BeautifulSoup(html.text,"lxml")
for link in soup.select("a[href$='.cms']"):
	url2 = link.get('href')
	result = urlparse(url2)
	if all([result.scheme, result.netloc]):
		filename = 'ph_ftrs51.txt'
		r = requests.get(url2)
		type(r)
		
		html = r.text
		soup = BeautifulSoup(html, "html5lib")
		type(soup)
		text = soup.get_text()
		
		words = re.findall('\w+', text)
		
		sw = nltk.corpus.stopwords.words('english')
		
		words_ns = []
		
		for word in words:
			if word not in sw:
				words_ns.append(word)
		
		phword = []
		file = open(filename)
		for line in file:
			phword.append(line.strip())
			
		word_freq = []
		
		for s in phword:
			n = operator.countOf(words_ns, s)
			if n > 0:
				word_freq.append([s])
				word_freq.append([n])
		
		print(url2,'	frequency=	',word_freq)
		url3 = url2
	else:
		url2 = url3 + url2
		filename = 'ph_ftrs51.txt'
		r = requests.get(url2)
		type(r)
		
		html = r.text
		soup = BeautifulSoup(html, "html5lib")
		type(soup)
		text = soup.get_text()
		
		words = re.findall('\w+', text)
		
		sw = nltk.corpus.stopwords.words('english')
		
		words_ns = []
		
		for word in words:
			if word not in sw:
				words_ns.append(word)
		
		phword = []
		file = open(filename)
		for line in file:
			phword.append(line.strip())
			
		print(url2,'	frequency=	',word_freq)
		