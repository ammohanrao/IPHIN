import nltk
import requests
import urllib.request
from urllib.parse import urlparse
import bs4
import pandas as pd
import re
import operator
import gc
from nltk.tokenize import sent_tokenize, word_tokenize
from bs4 import BeautifulSoup
from pandas import read_csv
from urllib.parse import urlparse
import csv

lang_data = pd.read_csv(r"url_data.txt",usecols=[0],sep='\\t',engine='python')
url_data = pd.read_csv(r"url_data.txt",usecols=[1],sep='\\t',engine='python')

lang_word = []
for index, row in lang_data.iterrows():
	lang_word.append(row['language'])
	
url_site = []
for index, row in url_data.iterrows():
	url_site.append(row['site'])

ph_word0 = []
ph_word1 = []
ph_word2 = []
ph_word3 = []
ph_word4 = []
ph_word5 = []
ph_word6 = []
ph_word7 = []
ph_word8 = []
ph_word9 = []
ph_data = pd.read_csv(r"ph_ftrs51dic.csv",usecols=[0],sep=',',engine='python')	
for index, row in ph_data.iterrows():
	ph_word0.append(row['english'])
ph_data = pd.read_csv(r"ph_ftrs51dic.csv",usecols=[1],sep=',',engine='python')	
for index, row in ph_data.iterrows():
	ph_word1.append(row['urdu'])
ph_data = pd.read_csv(r"ph_ftrs51dic.csv",usecols=[2],sep=',',engine='python')	
for index, row in ph_data.iterrows():
	ph_word2.append(row['punjabi'])
ph_data = pd.read_csv(r"ph_ftrs51dic.csv",usecols=[3],sep=',',engine='python')	
for index, row in ph_data.iterrows():
	ph_word3.append(row['marathi'])
ph_data = pd.read_csv(r"ph_ftrs51dic.csv",usecols=[4],sep=',',engine='python')	
for index, row in ph_data.iterrows():
	ph_word4.append(row['malayalam'])
ph_data = pd.read_csv(r"ph_ftrs51dic.csv",usecols=[5],sep=',',engine='python')	
for index, row in ph_data.iterrows():
	ph_word5.append(row['kannada'])
ph_data = pd.read_csv(r"ph_ftrs51dic.csv",usecols=[6],sep=',',engine='python')	
for index, row in ph_data.iterrows():
	ph_word6.append(row['hindi'])
ph_data = pd.read_csv(r"ph_ftrs51dic.csv",usecols=[7],sep=',',engine='python')	
for index, row in ph_data.iterrows():
	ph_word7.append(row['gujarati'])
ph_data = pd.read_csv(r"ph_ftrs51dic.csv",usecols=[8],sep=',',engine='python')	
for index, row in ph_data.iterrows():
	ph_word8.append(row['bengali'])
ph_data = pd.read_csv(r"ph_ftrs51dic.csv",usecols=[9],sep=',',engine='python')	
for index, row in ph_data.iterrows():
	ph_word9.append(row['telugu'])

def lang_id(counter):
	for s in lang_word:
		word = lang_word[counter]
	return word

def lang_url(counter):
	for s in lang_word:
		t = url_site[counter]
		return t

buf_word = '	frequency=	'

def ftch_ece(url_string):
	r = requests.get(url_string)
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
	word_freq = []
	for w in ph_word0:
		n = operator.countOf(words_ns, w)
		if n > 0:
			word_freq.append([w])
			word_freq.append([n])	
	
	return url,buf_word,word_freq

def ftch_cms(url_string):
	r = requests.get(url_string)
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
	word_freq = []
	for w in ph_word0:
		n = operator.countOf(words_ns, w)
		if n > 0:
			word_freq.append([w])
			word_freq.append([n])	
	
	return url_string,buf_word,word_freq	

def ftch_asp(url_string):
	r = requests.get(url_string)
	type(r)
	html = r.text
	soup = BeautifulSoup(html, "html5lib")
	type(soup)
	text = soup.get_text()	
	words = word_tokenize(text)	
	word_freq = []	
	count = 0
	for s in ph_word9:
		t = ph_word0[count]
		count += 1
		n = operator.countOf(words, s)
		if n > 0:
			word_freq.append([t])
			word_freq.append([n])		
	return url_string,buf_word,word_freq	
	
count = 0
for s in lang_word:
	t = url_site[count]
	count = count + 1
	if s == 'english':
		html = requests.get(t)
		soup = bs4.BeautifulSoup(html.text,"lxml")

		for link in soup.select("a[href$='.ece']"):
			url = link.get('href')
			print(ftch_ece(url))

		for link in soup.select("a[href$='.cms']"):
			url = link.get('href')
			result = urlparse(url)
			if all([result.scheme, result.netloc]):
				url3 = url
				print(ftch_cms(url))
			else:
				url = url3 + url
				print(ftch_cms(url))

	elif s == 'telugu':
		source = urllib.request.urlopen(t).read()
		soup = bs4.BeautifulSoup(source,'lxml')
		
		for link in soup.select("a[href$='.aspx']"):
			url2 = link.get('href')
			result = urlparse(url2)
			if all([result.scheme, result.netloc]):
				url3 = url2
				print(ftch_asp(url2))
			else:
				url2 = url3 + url2
				print(ftch_asp(url2))
	elif s == 'urdu':
		source = urllib.request.urlopen(t).read()
		soup = bs4.BeautifulSoup(source,'lxml')
		
		for link in soup.select("a[href$='.html']"):
			url2 = link.get('href')
			result = urlparse(url2)
			if all([result.scheme, result.netloc]):
				url3 = url2
				print(ftch_asp(url2))
			else:
				url2 = url3 + url2
				print(ftch_asp(url2))

	elif s == 'bengali':
		html = requests.get(t)
		soup = bs4.BeautifulSoup(html.text,"lxml")        
		
		links = soup.find_all('a')
		
		for link in links:
			try:
				url2 = link['href']
				result = urlparse(url2)
				
				if all([result.scheme, result.netloc]):	
					text = soup.get_text()	
					words = word_tokenize(text)					
					word_freq = []
					count=0;
					for s in ph_word8:
						e = ph_word0[count]						
						count = count +1
						n = operator.countOf(words, s)
						if n > 0:
							word_freq.append([e])
							word_freq.append([n])			
					print(url2,buf_word,word_freq)			
			except:
				pass