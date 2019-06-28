from KafNafParserPy import *
import os


file = open("wikiWhRhino.naf", "r", encoding="utf8")
content1 = file.read()


my_parser = KafNafParser('wikiWhRhino.naf')




# for term_obj in my_parser.get_terms():
    
#     print ('POS', term_obj.get_pos())


#if statement that selects and print specified lemmas

'''

for term_obj in my_parser.get_terms():
    if term_obj.get_lemma() == 'city':
        print ('lemma', term_obj.get_lemma())

'''
for term_obj in my_parser.get_terms():
    if term_obj.get_pos() == 'NOUN':
        print ('nouns', term_obj.get_lemma())
