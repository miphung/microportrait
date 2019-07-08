import spacy 
import os 

#test 

nlp = spacy.load("en_core_web_sm")
dirname = os.path.dirname(__file__)
#into microportraits folder
path = os.path.join(dirname,"../")

def fileread():
	for filename in os.listdir(path+"rawTest"):
		if filename.endswith(".txt"):
			orig = open(path+"rawTest/"+filename, "r", encoding="utf8")
			doc = nlp(orig.read())
			f = open(filename+ "SpDepPar.txt", "w", encoding="utf8")
			
			#for all nouns
			for chunk in doc.noun_chunks:
				#text itself
				f.write(chunk.text+" ")
				#lemma
				f.write(chunk.root.text+" ")
				#dependency
				f.write(chunk.root.dep_)
				f.write("\n")
			
			f.close()
fileread()