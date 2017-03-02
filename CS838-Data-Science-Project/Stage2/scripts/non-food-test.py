#!/usr/bin/python

import nltk
import re

if __name__ == "__main__":

# Feature 1 -
    # Ends with condition
    words = set()
    target = open("non_food_items.txt", 'r')
    for line in target:
        data = re.findall(r'\b(\w+ing)\b',line)
        data += re.findall(r'\b(\w+ed)\b',line)
        data += re.findall(r'\b(\w+y)\b',line)
        data += re.findall(r'\b(\w+ess)\b',line)
        #data += re.findall(r'\b(\w+le)\b',line) #improvement of 10 values
        for word in data:
            words.add(word)
    #print len(words)
    target.close()
    
    #for word in words:
    #    print word
    #print len(words)
    
# Feature 2 -
    # No of words condition
    count = 0
    target = open("non_food_items.txt", 'r')
    for line in target:
        word_count = len(line.split(" "))
        if word_count <= 1:
            count += 1
    #print count
    target.close()
    
# Feature 3 - 
target = open("non_food_items.txt", 'r')
for line in target:
    text = nltk.word_tokenize(line)
    tagged = nltk.pos_tag(text)
    for tag in tagged:
        print tag[tag]
    