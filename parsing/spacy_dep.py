import spacy 
import os 

#testing moreeee pt 3

nlp = spacy.load("en_core_web_sm")
dirname = os.path.dirname(__file__)
#into microportraits folder
path = os.path.join(dirname,"../")

def dep():
	for filename in os.listdir(path+"rawTest"):
		if filename.endswith(".txt"):
			orig = open(path+"rawTest/"+filename, "r", encoding="utf8")
			doc = nlp(orig.read())
			f = open(filename+ "SpDepPar.txt", "w", encoding="utf8")
			
			for token in doc:
				#text dep headText headPos
				f.write(token.text + " " +token.dep_ + " "+token.head.text + " "+ token.head.pos_ +" [")
				#temp = []
				for child in token.children:
					f.write(child.text+ " ")
				# for item in temp:
				# 	f.write(item)
				f.write("] \n")
			
			f.close()
dep()