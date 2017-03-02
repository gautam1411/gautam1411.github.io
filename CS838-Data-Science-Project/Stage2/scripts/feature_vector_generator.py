#!/usr/bin/python
#Generates feature vector from the data for machine learning
#Format - ['ends_in','no_of_words','contains_an_adjective','label']

import re
import nltk

map = {}

def feature_endsin(line):
    if re.findall(r'\b(\w+ing)\b',line) or \
    re.findall(r'\b(\w+ed)\b',line) or \
    re.findall(r'\b(\w+y)\b',line) or \
    re.findall(r'\b(\w+ian)\b',line) or \
    re.findall(r'\b(\w+can)\b',line) or \
    re.findall(r'\b(\w+ess)\b',line):
        return 1
    else:
        return 0
        
def feature_noofwords(line):
    n = len(line.split(" "))
    if n == 1:
        return 1
    else:
        return 0
    
def feature_contains_adj(line):
    adj = 0
    line = nltk.word_tokenize(line)
    line = nltk.pos_tag(line)
    for i in range(len(line)):
        if "JJ" in line[i][1]:
            adj = 1
            break
    if adj == 1:
        return 1
    else:
        return 0

def feature_contains_noun(line):
    noun = 0
    line = nltk.word_tokenize(line)
    line = nltk.pos_tag(line)
    for i in range(len(line)):
        if "NN" in line[i][1]:
            noun = 1
            break
    if noun == 1:
        return 1
    else:
        return 0

def feature_contains_verb(line):
    verb = 0
    line = nltk.word_tokenize(line)
    line = nltk.pos_tag(line)
    for i in range(len(line)):
        if "VB" in line[i][1]:
            verb = 1
            break
    if verb == 1:
        return 1
    else:
        return 0

def feature_length_check(line):
    if len(line) >= 10:
        return 1
    else:
        return 0
     
if __name__ == "__main__":
    words = set()
    nf_target = open("non_food_items_jugaad.txt", "r")
    f_target = open("food_items_jugaad.txt", "r")
    nf_writer = open("non_food_feature_vector_data_.txt","w")
    f_writer = open("food_feature_vector_data_.txt","w")
    count = 0
    tot = 0
    for line in nf_target:
        instance = []
        f_endsin = feature_endsin(line)
        f_noofwords = feature_noofwords(line)
        f_contains_adj = feature_contains_adj(line)
        f_contains_noun = feature_contains_noun(line)
        f_contains_verb = feature_contains_verb(line)
        f_length_check = feature_length_check(line)
        #if f_contains_noun:
        #    count += 1
        #tot += 1
        instance.append(str(f_endsin))
        instance.append(str(f_noofwords))
        instance.append(str(f_contains_adj))
        instance.append(str(f_contains_noun))
        instance.append(str(f_contains_verb))
        instance.append(str(f_length_check))
        instance.append(str(0))
        instance = ",".join(instance)
        nf_writer.write(instance + "\n")
    nf_target.close()
    nf_writer.close()
    
    for line in f_target:
        instance = []
        f_endsin = feature_endsin(line)
        f_noofwords = feature_noofwords(line)
        f_contains_adj = feature_contains_adj(line)
        f_contains_noun = feature_contains_noun(line)
        f_contains_verb = feature_contains_verb(line)
        f_length_check = feature_length_check(line)
        #if f_contains_noun:
        #    count += 1
        #tot += 1
        instance.append(str(f_endsin))
        instance.append(str(f_noofwords))
        instance.append(str(f_contains_adj))
        instance.append(str(f_contains_noun))
        instance.append(str(f_contains_verb))
        instance.append(str(f_length_check))
        instance.append(str(1))
        instance = ",".join(instance)
        f_writer.write(instance + "\n")
    f_target.close()
    f_writer.close()
    
    
    