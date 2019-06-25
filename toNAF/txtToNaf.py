import spacy_to_naf
import spacy
import os
import datetime

nlp = spacy.load("en_core_web_sm")

def fileread():
	for filename in os.listdir("C://Users//gwc//REU//microportrait//rawTest"):
		if filename.endswith(".txt"):
			orig = open("C://Users//gwc//REU//microportrait//rawTest//"+filename, "r", encoding="utf8")
			f = open(filename.replace(".txt", ".naf"), "w", encoding="utf8")
			text = " "
			for line in orig.read():
				text += line 
			#datetime.datetime.now() may just be datetime.now() depending on python version
			NAF = spacy_to_naf.text_to_NAF(text,nlp,dct=datetime.datetime.now(), layers={'raw', 'text', 'terms', 'entities'})
			f.write(spacy_to_naf.NAF_to_string(NAF))
			f.close()
fileread()