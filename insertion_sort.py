#! /usr/bin/env python3

'''
Michael Patel
CSC 505
Spring 2018

insertion_sort.py
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

# insertion sort algorithm
def insertionSort(inputList, compare): # in place aka modify list, not create new one
    #global numCompare #

    for i in range(1, len(inputList)): # move through 1 element at a time
        current = inputList[i] # current item will be checked against those already in sorted sublist
        location = i # location of current item

        while(location > 0):
            if(compare(current, inputList[location-1]) == LESS_THAN): # current item < element in sorted sublist
                inputList[location] = inputList[location-1] # shift sublist elements up 1 spot
                location = location - 1 # shift locations up 1 spot, spot (i-1) is free to insert current item
            else:
                break # current item will be at end of sorted sublist

        inputList[location] = current # insert current element into sorted sublist

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
sortedList = insertionSort(inputList, compare)
finish = getTime() # finish time for algorithm
####################################################################################################
#
# print out sorted list to console
printSortedList(sortedList)

# print out runtime and comparisons
printRuntimeAndComparisons(finish, start, numCompare)