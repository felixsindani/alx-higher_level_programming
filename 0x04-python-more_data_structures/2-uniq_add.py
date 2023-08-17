#!/usr/bin/python3
# function that adds all unique integers 
# in a list (only once for each integer).
def uniq_add(my_list=[]):
    every_unique_list = set(my_list)
    num = 0

    for i in every_unique_list:
        num += i

    return (num)
