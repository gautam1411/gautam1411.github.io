#!/usr/bin/python

if __name__ == "__main__":
    
    nfood = open("non_food_items_jugaad.txt", "r")
    food = open("food_items_jugaad.txt", "r")
    
    count = 0
    total = 0
    for line in nfood:
        count += 1
        total += len(line)
    avg = float(total)/count
    print "nfood avg", avg
    
    count = 0
    total = 0
    avg = 0
    for line in food:
        count += 1
        total += len(line)
    avg = float(total)/count
    print "food avg", avg
    
    nfood.close()
    food.close()
    