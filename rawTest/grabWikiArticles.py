#using Wikipedia to pull out the main articles

import wikipedia as wk

art1 = wk.page("Indian rhinoceros")
ih = open("wikiIndianRhino.txt","w", encoding="utf-8")
a1 = art1.content
#for i in range(len(a1)):
ih.write(a1)
ih.close()
