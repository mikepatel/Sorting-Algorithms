#! /usr/bin/env python3

'''
Michael Patel
CSC 505
Spring 2018

merge_sort.py

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
# merge
def merge(list1, list2, compare): # merge the two sorted sublists together to create a new sorted list
    sortedList = [] # new sorted list

    while((len(list1) != 0) and (len(list2) != 0)): # while neither list is empty
        if(compare(list1[0], list2[0]) == LESS_THAN): # if the first item in list1 is < first item in list2
            sortedList.append(list1[0]) # add item to new list
            list1.remove(list1[0]) # remove item from sublist

        else: # first item in list1 <= first item in list2
            sortedList.append(list2[0]) # add item to new list
            list2.remove(list2[0]) # remove item from sublist

    # at least one sublist is empty
    if(len(list1) == 0): # first sublist is empty
        sortedList = sortedList + list2 # add the sorted elements of sublist2 to the new sorted list
    else: # second sublist is empty
        sortedList = sortedList + list1 # add the sorted elements of sublist1 to the new sorted list

    return sortedList

# merge sort algorithm
def mergeSort(inputList): # will create a new sorted list
    if(len(inputList) == 0): # list is empty
        return inputList
    elif(len(inputList) == 1): # list only has 1 element
        return inputList
    else:
        halfpoint = len(inputList) / 2 # determine the half-way location
        list1 = mergeSort(inputList[:halfpoint])
        list2 = mergeSort(inputList[halfpoint:])
        return merge(list1, list2, compare)

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
sortedList = mergeSort(inputList)
finish = getTime() # finish time for algorithm
####################################################################################################
#
# print out sorted list to console
printSortedList(sortedList)

# print out runtime and comparisons
printRuntimeAndComparisons(finish, start, numCompare)