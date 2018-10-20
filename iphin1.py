import nltk
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
import operator

response = requests.get("http://www.thehindu.com/archive/web/2018/10/20/").text
soup = BeautifulSoup(response,"lxml")

for link in soup.select("a[href$='.ece']"):    
	url = link.get('href')
	filename = 'ph_ftrs51.txt'
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
	print(url,'	frequency=	',word_freq)








