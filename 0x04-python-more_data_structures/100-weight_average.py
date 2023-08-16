#!/usr/bin/python3
# function that returns the weighted
# average of all integers tuple
def weight_average(my_list=[]):
    if not my_list:
        return 0
    number = 0
    all_intergers = 0
    for tup in my_list:
        number += tup[0] * tup[1]
        all_intergers += tup[1]

    return (number / all_intergers)
