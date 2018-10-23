import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from nltk.tokenize import sent_tokenize, word_tokenize
import operator
import pandas as pd
from pandas import read_csv

response = requests.get("http://epaperdaily.com/indian/daily-sahafat-mumbai-lucknow-delhi-india.html").text
soup = BeautifulSoup(response,"lxml")

ph_data = pd.read_csv(r"ph_ftrs51dic.csv",usecols=[1])
phword = []
for index, row in ph_data.iterrows():
	phword.append(row['urdu'])
	
for link in soup.select("a[href$='.html']"):
	url2 = link.get('href')
	result = urlparse(url2)	
	if all([result.scheme, result.netloc]):
		r = requests.get(url2)
		type(r)
		
		html = r.text
		soup = BeautifulSoup(html, "html5lib")
		type(soup)
		text = soup.get_text()	
		words = word_tokenize(text)		
	
		word_freq = []
		
		for s in phword:			
			n = operator.countOf(words, s)
			if n > 0:
				word_freq.append([s])
				word_freq.append([n])
		
		print(url2,'	frequency=	',word_freq)