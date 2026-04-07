"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    """dummy comment"""
    
    if list_one==list_two:
        return EQUAL
    
    length_one=len(list_one)
    length_two=len(list_two)
    
    if length_one<length_two:
        if length_one==0:
            return SUBLIST
        for index_two in range(length_two-length_one+1):
            if list_one==list_two[index_two:index_two+length_one]:
                return SUBLIST
        return UNEQUAL
    
    if length_one>=length_two:
        if length_two==0:
            return SUPERLIST
        for index_one in range(length_one-length_two+1):
            if list_two==list_one[index_one:index_one+length_two]:
                return SUPERLIST
        return UNEQUAL
    return UNEQUAL
