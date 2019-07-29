import spacy
from KafNafParserPy.KafNafParserMod import *
import neuralcoref



# study of how they added dependents and how it can be used for coreference

def generate_coref(corefx):
    '''
    Corrently, this adds a coreference section to the naf file successfully.
    However, the formatting is wrong and need to be changed to fit with the coref layer correctly
    :param corefx:
    :return: naf (layer?) object
    '''
    coreferences = []


    try:
        for list in corefx:
            my_cr = Ccoreference()
            my_cr.set_id(list[1])
            my_cr.set_type('entity')
            my_cr.add_span('t10')
            #my_cr.add_external_reference(exref)

            coreferences.append(my_cr)
    except Exception as e:
        print(sys.stderr, str(e))
    return coreferences



# dealing with getting files open and raw text extracted and processed

file = open("WikiWhRhino.naf", "r", encoding="utf8" )
content1 = file.read()

the_str ="""" """

my_parser = KafNafParser('WikiWhRhino.naf')

for raw_word in my_parser.get_raw():
    the_str= the_str+raw_word

# V test string for faster return time V  ^ must comment out file opening section first ^
#the_str = "Sam is the coolest person. She goes to the club. It is her favorite place. JAMMER is her dog's name. he is an abomination. The dog, JAMMER is maxed out"

nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)

doc = nlp(the_str)


def coref():
    '''
    gathers all the coreferences in a doc,
    deletes duplicates (for some reason was adding the same line PER word in the reference)
    reduces main mention to a single head noun (needs work: only works for multi word expressions. for single references it pulles its head verb instead)
    adds index/termid for main head (mostly nouns)
    :return: a formatted string resembling [entity[mentions, mentions] head/index(termid),number of mentions
    '''
    strang = []
    biggerstrang = []
    strangmem = []
#todo get span for mentions, and/or original ent

#todo make this store the string elements in a list instead, and then store that list in a list

    for token in doc:
        if str(token._.coref_clusters) != "[]":
            if str(token._.coref_clusters) not in strangmem:
                strang.append(str(token._.coref_clusters))
                strangmem.append(str(token._.coref_clusters))
                strang.append(token.head.text)
                strang.append('t' + str(token.head.i))
                strang.append(str(len(token._.coref_clusters[-1].mentions)))
                biggerstrang.append(strang)
            strang = []
    return biggerstrang


CRout = coref()
#print ('\n# output: [entity[mentions, mentions] head/index(termid) entitylength \n \n', coref())

# section that attempts to pull out specific referenced nouns. Please ignore for now.
list1 = []
list2 = []
for ref in coref():
    list1.append(ref[1])
    if ref[1] == 'rhino' or 'rhinoceros':
        list2.append(ref[2])
    print(ref)
    #print(dab[2])
print('corefs with rhino', list2)


# takes the coref() out list and turns it into a naf onj, then adds the naf layer object to the naf file
for c in generate_coref(CRout):
    my_parser.add_coreference(c)

my_parser.dump()