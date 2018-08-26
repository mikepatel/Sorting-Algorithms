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

    if(obj1 < obj2):
        return LESS_THAN
    elif (obj1 > obj2):
        return GREATER_THAN
    elif(obj1 == obj2):
        return EQUAL_TO

####################################################################################################
# heapify
def heapify(inputList, heapSize, nodeLoc, compare):
    pseudoRootLoc = nodeLoc # node (the root of the subtree - set the root as the largest value since doing max heap)
    leftOfNode = 2 * nodeLoc + 1 # node is at 2n
    rightOfNode = 2 * nodeLoc + 2

    # Left side
    if(leftOfNode < heapSize): # does a leaf of the subtree node/root exist on left side?
        if(compare(inputList[leftOfNode], inputList[nodeLoc]) == GREATER_THAN): # the left leaf child value > node value
            pseudoRootLoc = leftOfNode # update the location of the node

    # Right side
    if(rightOfNode < heapSize): # does a leaf of the subtree node/root exist on right side?
        if(compare(inputList[rightOfNode], inputList[pseudoRootLoc]) == GREATER_THAN): # the right leaf child value > node value
            pseudoRootLoc = rightOfNode # update the location of the node

    # node update occurred, now reflect in values
    if(pseudoRootLoc != nodeLoc): # node location has been updated
        inputList[pseudoRootLoc], inputList[nodeLoc] = inputList[nodeLoc], inputList[pseudoRootLoc] # swap values

        # call heapify() to repair the heap as swapping may violate max heap properties
        heapify(inputList, heapSize, pseudoRootLoc, compare)

# heap sort algorithm
def heapSort(inputList): # in place aka modify list, not create new one
    heapSize = len(inputList) # get size of heap

    # build max heap
    for i in range(heapSize, -1, -1):
        heapify(inputList, heapSize, i, compare)

    # sort in ascending order
    for i in range(heapSize-1, 0, -1):
        inputList[0], inputList[i] = inputList[i], inputList[0] # swap last element with first
        heapify(inputList, i, 0, compare) # call heapify() to repair the heap as swapping may violate max heap properties

    return inputList # sorted

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
sortedList = heapSort(inputList)
finish = getTime() # finish time for algorithm
####################################################################################################
#
# print out sorted list to console
printSortedList(sortedList)

# print out runtime and comparisons
printRuntimeAndComparisons(finish, start, numCompare)