import spacy_to_naf
import spacy
import os
import datetime

nlp = spacy.load("en_core_web_sm")

dirname = os.path.dirname(__file__)
#into microportraits folder
path = os.path.join(dirname,"../")

def fileread():
	for filename in os.listdir(path+"rawTest"):
		if filename.endswith(".txt"):
			orig = open(path+"rawTest/"+filename, "r", encoding="utf8")
			f = open(filename.replace(".txt", ".naf"), "w", encoding="utf8")
			text = " "
			for line in orig.read():
				text += line 
			#datetime.datetime.now() may just be datetime.now() depending on python version
			NAF = spacy_to_naf.text_to_NAF(text,nlp,dct=datetime.datetime.now(), layers={'raw', 'text', 'terms', 'entities', 'deps', 'chunks'})
			f.write(spacy_to_naf.NAF_to_string(NAF))
			f.close()
fileread()

