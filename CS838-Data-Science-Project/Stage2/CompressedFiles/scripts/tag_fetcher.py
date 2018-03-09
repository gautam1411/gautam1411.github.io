#!/usr/bin/python
#Read content from filtered CSV file and display that information

import csv
import nltk
import pandas as pd
import re
from operator import itemgetter

content = []
filtered_content = []

p_set = set()
n_set = set()


def tag_extractor(token):
    #global p_set, n_set
    content = ""
    flag = 0
    category = 0
    #for i in range(len(token)):
    i=0
    while i < len(token): 
        if token[i] == "<":
            i += 1
            if i < len(token) and token[i] == "/":
                flag = 2
                i += 2
            
            if i < len(token) and token[i] == "p":
                i += 1
                if i < len(token) and token[i] == ">":
                    i += 1
                    flag = 1
                    category = 1
            if i < len(token) and token[i] == "n":
                i += 1
                if i < len(token) and token[i] == ">":
                    i += 1
                    flag = 1
                    category = 2
        if flag == 1:
            content += token[i]
        elif flag == 2:
            if category == 1:
                p_set.add(content)
            else:
                n_set.add(content)
            content = ""
            flag = 0
        i += 1

# Read the CSV into a pandas data frame (df)
#   With a df you can do many things
#   most important: visualize data with Seaborn
df = pd.read_csv('naman_filtered.csv', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

# Or export it in many ways, e.g. a list of tuples
tuples = [tuple(x) for x in df.values]

for tup in tuples:
    review = tup[1].decode('utf-8')
    tag_extractor(review.lower())
    
print "positives", len(p_set)
print "negatives", len(n_set)

#for entry in p_set:
#    print entry
    


target = open("food_items.txt", 'w')
for entry in p_set:
    target.write((entry+"\n").encode('utf-8'))

target = open("non_food_items.txt", 'w')
for entry in n_set:
    target.write((entry+"\n").encode('utf-8'))


