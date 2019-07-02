from KafNafParserPy import *
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,"../../toNAF/")
file = open(filename+"wikiWhRhino.naf", "r", encoding="utf8")

my_parser = KafNafParser('wikiWhRhino.naf')


for term_obj in my_parser.get_terms():
    if term_obj.get_pos() == 'NOUN':
        print ('nouns', term_obj.get_lemma())