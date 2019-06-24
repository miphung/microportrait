#using Wikipedia to pull out the main and SpaCy to format the text
#code found on Stack Overflow by Omid Raha, https://stackoverflow.com/questions/23351103/extract-the-main-article-text-from-a-wikipedia-page-using-python
#SpaCy code found in github page: https://github.com/explosion/spaCy/issues/93#issuecomment-138773719

from __future__ import unicode_literals, print_function
import spacy
spacy.load('en_core_web_sm')
from spacy.lang.en import English
import wikipedia as wk

nlp = English()

#the first wiki article 
art1 = wk.page("Indian rhinoceros")
ih = open("wikiIndianRhino.txt","w", encoding="utf-8")
a1 = nlp(art1.content)
for s in a1.sents:
	ih.write(asent)
ih.close()
'''
#second wiki article on black rhinos
art2 = wk.page("Black rhinoceros")
ih = open("wikiBlRhino.txt","w", encoding="utf-8")
a2 = nlp(art2.content)
bsent = [s.string.strip() for s in a2.sents]
ih.write(bsent)
ih.close()

#third wiki article on white rhinos
art3 = wk.page("White rhinoceros")
ih = open("wikiWhRhino.txt","w", encoding="utf-8")
a3 = nlp(art3.content)
csent = [s.string.strip() for s in a3.sents]
ih.write(csent)
ih.close()

#fourth wiki article on rhinos
art4 = wk.page("Rhinoceros")
ih = open("wikiRhino.txt","w", encoding="utf-8")
a4 = nlp(art4.content)
dsent = [s.string.strip() for s in a4.sents]
ih.write(dsent)
ih.close()
'''