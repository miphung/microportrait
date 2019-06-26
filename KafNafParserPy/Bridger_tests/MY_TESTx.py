from KafNafParserPy import *


file = open("wikiWhRhino.naf", "r", encoding = 'utf8')
content1 = file.read()


my_parser = KafNafParser('wikiWhRhino.naf')


'''

for term_obj in my_parser.get_terms():
    
    print ('lemma', term_obj.get_lemma())

#print(content1.get_pos('noun'))

'''


for term_obj in my_parser.get_terms():
    if term_obj.get_lemma() == 'city':
        print ('lemma', term_obj.get_lemma())

