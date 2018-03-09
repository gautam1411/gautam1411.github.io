#!/usr/bin/python
#Read from the reviews CSV file, process data and write filtered data to another csv file

import csv

content = []
filtered_content = []
file = open("data.txt", "r")
for line in file:
    content.append(line)

index = 1
for line in content:
    filtered_instance = []
    print "instace", index
    index += 1
    rating = float(line[1]+line[2]+line[3]) # Extract the rating
    filtered_instance.append(rating)
    for i in range(6,len(line)): # Find out the starting of the rating
        if line[i] == " ":
            continue
        else:
            break
    string_cnt = 0
    review = ""
    for j in range(i,len(line)): #Detect two strings and capture review
        if line[j] != '"':
            review += line[j]
            continue
        elif line[j] == ",":
            continue
        else:
            string_cnt += 1
            if string_cnt == 2:
                break
    filtered_instance.append(review)
    
    restaurant = ""
    for k in range(j+1,len(line)): #Detect restaurant name
        if line[k] == '"':
            break
        restaurant += line[k]
    filtered_instance.append(restaurant)
    
    for l in range(k+1,len(line)): #Detect the starting of the city name
        if line[l] == '"':
            break
    city = ""
    string_cnt = 0
    for m in range(l+1,len(line)): #Capture the city name and detect two strings
        if line[m] == ",":
            continue
        if line[m] == '"':
            string_cnt += 1
            if string_cnt == 2:
                break
        else:
            city += line[m]
    filtered_instance.append(city)
    '''
    votes = ""
    string_cnt = 0
    for n in range(m+1,len(line)): #Capture the number of votes and detect two strings
        if line[n] == '"':
            string_cnt += 1
            if string_cnt == 2:
                break
        else:
            if line[n].isdigit():
                votes += line[n] 
    votes = int(votes)
    filtered_instance.append(votes)
    cost_for_two = ""
    for o in range(n+1,len(line)): #Captue the cost for two people
        if line[o].isdigit():
            cost_for_two += line[o] 
    cost_for_two = int(cost_for_two)
    filtered_instance.append(cost_for_two)
    '''
    filtered_content.append(filtered_instance) #Add the tuple list to the parent list
'''
for tuple in filtered_content: 
    print tuple, "\n"

    
with open('filtered_dataset-2.csv', 'w') as outcsv:   
    #configure writer to write standard csv file
    writer = csv.writer(outcsv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    #writer.writerow(['number', 'text', 'number'])
    for tuple in filtered_content:
        #Write item to outcsv
        writer.writerow([tuple[0], tuple[1], tuple[2], tuple[3]])
'''