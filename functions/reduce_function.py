# import functools
from functools import reduce

collections = [11, 22, 33, 44, 55, 66]

def totalCollection(x, y):
    return x + y

grandTotal = reduce(totalCollection, collections) # it will add all the values from the collections based on the argument given in aboce functions

print(grandTotal)

def divCollect(x, y):
    return x * y

grnftot = reduce(divCollect, collections)

print(grnftot)