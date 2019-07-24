import spacy
from KafNafParserPy.KafNafParserMod import *
import neuralcoref

'''

# study of how they added dependents and how it can be used for coreference 

def generate_coref(self, list_term_ids):
    # This will creathe dependency
    dependencies = []
    try:
        terms_from = [list_term_ids[idx] for idx in range(self.begin_from, self.end_from)]
        terms_to = [list_term_ids[idx] for idx in range(self.begin_to, self.end_to)]
        for t_from in terms_from:
            for t_to in terms_to:
                ##Creating comment

                my_dep = Ccoreference()
                my_dep.set_id(cid)
                my_dep.set_type(ctype)
                my_dep.add_span(cspan)
                my_dep.add_external_reference(exref)

                dependencies.append(my_dep)
    except Exception as e:
        print(sys.stderr, str(e))
    return dependencies

'''

# dealing with getting files open and raw text extracted and processed

file = open("wikiWhRhino.naf", "r", encoding="utf8" )
content1 = file.read()

the_str ="""" """

my_parser = KafNafParser('wikiWhRhino.naf')

for raw_word in my_parser.get_raw():
    the_str= the_str+raw_word

# V test string for faster return time V  ^ must comment out file opening section first ^
#the_str = "Sam is the coolest person. She goes to the club. It is her favorite place. JAMMER is her dog's name. he is a buff dog. The dog, JAMMER can run very fast"

nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)

doc = nlp(the_str)


def coref():
    '''
    gathers all the coreferences in a doc,
    deletes duplicates (for some reason was adding the same line PER word in the reference)
    reduces main mention to a single head noun (needs work: only works for multi word expressions. for single references it pulles its head verb instead)
    adds index/termid for main head (mostly nouns)
    :return: a formatted string resembling [entity[mentions, mentions] head/index(termid),entitylength
    '''
    strang = ''

#todo get span for mentions, and/or original ent

    for token in doc:
        if str(token._.coref_clusters) != "[]":
            if str(token._.coref_clusters) not in strang:
                strang += (str(token._.coref_clusters) + token.head.text + '/t' + str(token.head.i) + "," + str(len(token)) + "\n")
    return strang



print ('\n# output: [entity[mentions, mentions] head/index(termid) entitylength \n \n', coref())