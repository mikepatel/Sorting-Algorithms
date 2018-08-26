#! /usr/bin/env python3

'''
Michael Patel
CSC 505
Spring 2018

functions.py

'''
####################################################################################################
# Imports
import time
import sys

####################################################################################################
# get the time in milliseconds
def getTime():
    return int(round(time.time() * 1000))

# print sorted list
def printSortedList(sortedList):
    for i in sortedList:
        print(i)

# print runtime and number of comparisons
def printRuntimeAndComparisons(finish, start, numCompare):
    sys.stderr.write("runtime,%d\n" % int(finish - start))
    sys.stderr.write("comparisons,%d\n" % numCompare)

# comparison function
def cmp_to_key(mycmp): # convert a cmp= function into a key= function
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K

