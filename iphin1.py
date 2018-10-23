import nltk
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import operator
import gc
import pandas as pd
from pandas import read_csv

response = requests.get("http://www.thehindu.com/archive/web/2018/10/14/").text
soup = BeautifulSoup(response,"lxml")
ph_data = pd.read_csv(r"ph_ftrs51dic.csv",usecols=[0])

for link in soup.select("a[href$='.ece']"):    
	url = link.get('href')
	r = requests.get(url)
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
			words_ns.append(word.lower())
			
	phword = []
	for index, row in ph_data.iterrows():
		phword.append(row['english'])
	
	word_freq = []
	
	for s in phword:
		n = operator.countOf(words_ns, s)
		if n > 0:
			word_freq.append([s])
			word_freq.append([n])
	print(url,'	frequency=	',word_freq)
	del words_ns
	del phword
	del word_freq
	gc.collect()
