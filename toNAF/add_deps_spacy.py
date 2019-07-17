
import sys
import getopt
import os
import logging
import re

import argparse


from lxml import etree
from subprocess import Popen,PIPE




###Alpino class section

last_modified='20jun2019'
version="0.2"
this_name = 'Alpino to spaCy KAF/NAF dependency parser'
this_layer = 'deps'
config_filename = 'config.cfg'


class Calpino_dependency:


    def __init__(self, line):
        self.ok = True
        self.begin_from = self.begin_to = self.end_from = self.end_to = self.sentence = ''
        fields = line.split(' ')
        if len(fields) == 4:
            token_to = fields[0]
            match = re.match(r'(.+)/\[(\d+),(\d+)\]', token_to)
            if match is not None:
                self.lemma_to = match.group(1)
                self.begin_to = int(match.group(2))
                self.end_to = int(match.group(3))

                token_from = fields[2]
                match2 = re.match(r'(.+)/\[(\d+),(\d+)\]', token_from)
                if match2 is not None:
                    self.lemma_from = match2.group(1)
                    self.begin_from = int(match2.group(2))
                    self.end_from = int(match2.group(3))
                    self.relation = fields[1]
                    self.sentence = fields[3]
                else:
                    self.ok = False
            else:
                self.ok = False
        else:
            self.ok = False

    def get_sentence(self):
        return self.sentence

    def is_ok(self):
        return self.ok

    def __repr__(self):
        r = (self.begin_from, self.end_from, self.begin_to, self.end_to)
        return r

    def generate_dependencies(self, list_term_ids):
        # This will create dependency
        dependencies = []
        try:
            terms_from = [list_term_ids[idx] for idx in range(self.begin_from, self.end_from)]
            terms_to = [list_term_ids[idx] for idx in range(self.begin_to, self.end_to)]
            for t_from in terms_from:
                for t_to in terms_to:
                    ##Creating comment
                    str_comment = ' ' + self.relation + '(' + self.lemma_to + ',' + self.lemma_from + ') '

                    my_dep = Cdependency()
                    my_dep.set_from(t_to)
                    my_dep.set_to(t_from)
                    my_dep.set_function(self.relation)
                    my_dep.set_comment(str_comment)

                    dependencies.append(my_dep)
        except Exception as e:
            print(sys.stderr, str(e))
        return dependencies





### SpaCy dependency section
import spacy

nlp = spacy.load("en_core_web_sm")
dirname = os.path.dirname(__file__)
# into microportraits folder
path = os.path.join(dirname, "../")



def dep():

'''
opens specified file and runs it through spacy's pipeline
as well as formatting the output into a str line by line.
at the moment it only reads the raw text here,
but could be made to read from the <raw> section of a naf
out:
rhinoceros/[0,1] det The/[1,2] 0
'''
    orig = open("WikiWhRhino", "r", encoding="utf8")
    doc = nlp(orig.read())
    formatedStr = ''
    counter = -1
    sent = doc[1:4]
    for token in doc:
                # head relation dep sent(int)
        if token.sent != sent:
            counter = counter + 1
        formatedStr = formatedStr+(token.head.text + "/[" + str(0) + "," + str(1) + "]" + " " + token.dep_ + " " + token.text + "/[" + str(1) + "," + str(2) + "]" + " " + str(counter))
                # temp = []
        formatedStr += ("\n")
        sent = token.sent
    return formatedStr





# NAF file reading section.

from KafNafParserPy.KafNafParserMod import *

my_knaf = KafNafParser("WikiWhRhino_dep.naf")
sentences = []
current_sent = []
term_ids = []
current_sent_tid = []

lemma_for_termid = {}
termid_for_token = {}

for term in my_knaf.get_terms():
    term_id = term.get_id()
    lemma = term.get_lemma()
    lemma_for_termid[term_id] = lemma
    tokens_id = term.get_span().get_span_ids()
    for token_id in tokens_id:
        termid_for_token[token_id] = term_id

previous_sent = None
for token_obj in my_knaf.get_tokens():
    token = token_obj.get_text()
    sent = token_obj.get_sent()
    token_id = token_obj.get_id()

    ##To avoid using tokens that have no term linked
    if token_id not in termid_for_token:
        continue
    if sent != previous_sent and previous_sent != None:
        sentences.append(current_sent)
        current_sent = [token]
        term_ids.append(current_sent_tid)
        current_sent_tid = [termid_for_token[token_id]]
    else:
        current_sent.append(token)
        current_sent_tid.append(termid_for_token[token_id])
    previous_sent = sent

if len(current_sent) != 0:
    sentences.append(current_sent)
    term_ids.append(current_sent_tid)






### Naf adding code

for line in dep().splitlines():
    line = line.strip()
    my_dep = Calpino_dependency(line)
    if my_dep.is_ok():
        my_sentence_index = my_dep.get_sentence()
        list_term_ids = term_ids[int(my_sentence_index)]
        deps = my_dep.generate_dependencies(list_term_ids)
        for d in deps:
            my_knaf.add_dependency(d)



#add the dependency heading to the header
my_lp = Clp()
my_lp.set_name(this_name)
my_lp.set_version(version+'_'+last_modified)

my_lp.set_timestamp('*')

my_knaf.add_linguistic_processor(this_layer, my_lp)
my_knaf.dump()

sys.exit(0)

