from KafNafParserPy import *


file = open("naf_example.xml", "r")
content1 = file.read()


my_parser = KafNafParser('naf_example.xml')




for term_obj in my_parser.get_terms():
    
    print ('lemma', term_obj.get_lemma())


#if statement that selects and print specified lemmas

'''

for term_obj in my_parser.get_terms():
    if term_obj.get_lemma() == 'city':
        print ('lemma', term_obj.get_lemma())

'''
