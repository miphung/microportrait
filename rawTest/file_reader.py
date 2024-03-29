import spacy

from spacy.matcher import Matcher


### opens specified file ###

file = open("WWF_african_rhino.txt", "r")
content1 = file.read()
#print(content1)

### opens specified file ###


nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)

doc = nlp(content1)



###pattern test###

#pattern = [{"LEMMA": "African"}, {"POS": 'NNP'}]
#pattern = [{"POS": "NNP"}, {"POS": 'VB'}]
pattern = [{"POS": "NNP"}]

###pattern test###


### prints patterns if found ###

matcher.add("DOWNLOAD_THINGS_PATTERN", None, pattern)

matches = matcher(doc)

print("Total matches found:", len(matches))

for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
