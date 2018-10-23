import bs4 as bs
from bs4 import BeautifulSoup
import requests
import urllib.request
from urllib.parse import urlparse
from nltk.tokenize import sent_tokenize, word_tokenize
import operator
import pandas as pd
from pandas import read_csv

source = urllib.request.urlopen('http://archives.eenadu.net/10-21-2018/home.aspx').read()
soup = bs.BeautifulSoup(source,'lxml')

ph_data = pd.read_csv(r"ph_ftrs51dic.csv",usecols=[9])
phword = []
for index, row in ph_data.iterrows():
	phword.append(row['telugu'])
	
for link in soup.select("a[href$='.aspx']"):
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
		
		
