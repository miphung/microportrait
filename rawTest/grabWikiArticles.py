#using Wikipedia to pull out the main articles

import wikipedia as wk
'''
#the first wiki article 
art1 = wk.page("Indian rhinoceros")
ih = open("wikiIndianRhino.txt","w", encoding="utf-8")
a1 = art1.content
ih.write(a1)
ih.close()

#second wiki article on black rhinos
art2 = wk.page("Black rhinoceros")
ih = open("wikiBlRhino.txt","w", encoding="utf-8")
ih.write(art2.content)
ih.close()

#third wiki article on white rhinos
art3 = wk.page("White rhinoceros")
ih = open("wikiWhRhino.txt","w", encoding="utf-8")
ih.write(art3.content)
ih.close()
'''
#fourth wiki article on rhinos
art4 = wk.page("Rhinoceros")
ih = open("wikiRhino.txt","w", encoding="utf-8")
ih.write(art4.content)
ih.close()


