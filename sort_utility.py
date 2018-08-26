#! /usr/bin/env python3

'''
Michael Patel
CSC 505
Spring 2018

sort_utility.py
'''
####################################################################################################
# Imports
from functions import *
from constants import *

####################################################################################################
# GLOBALs
numCompare = 0
inputLineCount = 1
inputList = [] # original list
sortedList = [] # sorted list

####################################################################################################
# Comparison function
def compare(obj1, obj2):
    global numCompare
    numCompare = numCompare + 1

    if (obj1 < obj2):
        return LESS_THAN
    elif (obj1 > obj2):
        return GREATER_THAN
    elif (obj1 == obj2):
        return EQUAL_TO

####################################################################################################
# use list.sort()
def utilSort(inputList, compare):
    inputList.sort(key=cmp_to_key(compare))  # sorts in place
    return inputList
####################################################################################################
# read in the original list
while True:
    try:
        line = input()
        inputList.append(line)

    except Exception as e:
        #print("Exception: " + str(e))
        if(inputLineCount == 1):
            inputLineCount = inputLineCount + 1
            #print("line count is: " + str(inputLineCount))
        else:
            break
#print(inputList)

####################################################################################################
# running of the algorithm
start = getTime() # start time for algorithm
sortedList = utilSort(inputList, compare)
finish = getTime() # finish time for algorithm
####################################################################################################
#
# print out sorted list to console
printSortedList(sortedList)

# print out runtime and comparisons
printRuntimeAndComparisons(finish, start, numCompare)
