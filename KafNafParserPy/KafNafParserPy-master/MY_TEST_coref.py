from KafNafParserPy.KafNafParserMod import *
import spacy
import neuralcoref

file = open("wikiWhRhino.naf", "r", encoding="utf8" )
content1 = file.read()

the_str ="""" """

my_parser = KafNafParser('wikiWhRhino.naf')


for raw_word in my_parser.get_raw():
    the_str= the_str+raw_word



nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)

doc = nlp(the_str)
for cluster in doc._.coref_clusters:
    print(cluster)