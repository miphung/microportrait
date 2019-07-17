#using Wikipedia to pull out the main and SpaCy to format the text
#code found on Stack Overflow by Omid Raha, https://stackoverflow.com/questions/23351103/extract-the-main-article-text-from-a-wikipedia-page-using-python
#SpaCy code found in github page: https://github.com/explosion/spaCy/issues/93#issuecomment-138773719

from __future__ import unicode_literals, print_function
import spacy
import wikipedia as wk
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

nlp = spacy.load("en_core_web_sm")
'''
#the first wiki article 
art1 = wk.page("Indian rhinoceros")
ih = open("wikiIndianRhino.txt","w", encoding="utf-8")
a1 = nlp(art1.content)
for s in a1.sents:
	ih.write(s.text)
	ih.write("\n")
ih.close()

#second wiki article on black rhinos
art2 = wk.page("Black rhinoceros")
ih = open("wikiBlRhino.txt","w", encoding="utf-8")
a2 = nlp(art2.content)
for s in a2.sents:
	ih.write(s.text)
	ih.write("\n")
ih.close()

#third wiki article on white rhinos
art3 = wk.page("White rhinoceros")
ih = open("wikiWhRhino.txt","w", encoding="utf-8")
a3 = nlp(art3.content)
for s in a3.sents:
	ih.write(s.text)
	ih.write("\n")
ih.close()

#fourth wiki article on rhinos
art4 = wk.page("Rhinoceros")
ih = open("wikiRhino.txt","w", encoding="utf-8")
a4 = nlp(art4.content)
for s in a4.sents:
	ih.write(s.text)
	ih.write("\n")
ih.close()
'''
f = open("wp.txt",'w', encoding='utf8')
# wpage = urlopen("https://www.washingtonpost.com/photography/2019/07/08/no-mans-land-plight-northern-white-rhino/?noredirect=on&utm_term=.efa91d2e177f")
# page = wpage.read()
# soup = BeautifulSoup(page, "html.parser")
wpage = "https://www.washingtonpost.com/photography/2019/07/08/no-mans-land-plight-northern-white-rhino/?noredirect=on&utm_term=.efa91d2e177f"
result = requests.get(wpage)
c = result.content
soup = BeautifulSoup(c, features='lxml')

art_text = ''
t = soup.find('div', attrs={"class": "moat-trackable pb-f-theme-dark pb-f-dehydrate-false pb-f-async-false full pb-feature pb-layout-item pb-f-article-article-body"}).findAll('p')
for x in t:
	art_text += ''.join(x.findAll(text = True))+'\n'
f.write(art_text)
f.close()