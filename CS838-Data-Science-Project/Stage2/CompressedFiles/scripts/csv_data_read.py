#!/usr/bin/python
#Read content from filtered CSV file and display that information

import csv
import nltk
import pandas as pd
import re
from operator import itemgetter

content = []
filtered_content = []


# Read the CSV into a pandas data frame (df)
#   With a df you can do many things
#   most important: visualize data with Seaborn
df = pd.read_csv('filtered_dataset.csv', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

# Or export it in many ways, e.g. a list of tuples
tuples = [tuple(x) for x in df.values]

all_words = []
for tup in tuples:
    review = tup[1].decode('utf-8')
    tokens = nltk.word_tokenize(review)
    for token in tokens:
        full_word = []
        for element in token:
            #regex = r"([a-zA-Z])"
            #if re.search(regex, element):
            if element.isalpha():
                full_word += element
        if len(full_word) >= 3:
            all_words.append(token)
            
wordlist = nltk.FreqDist(all_words)
new_word_list = []
for word in wordlist:
    new_word_list.append([word, wordlist[word]])
for word in new_word_list:
    print word
new_word_list = sorted(new_word_list, key=itemgetter(1), reverse=True)

#wordlist.sort(key=lambda x: x[1])

# Flush the word frequencies in a file
target = open("word-freq.txt", 'w')
for word in new_word_list:
    target.write((word[0] + " " + str(word[1]) + "\n").encode('utf-8'))


