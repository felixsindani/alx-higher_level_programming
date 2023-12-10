#!/usr/bin/python3
# function that finds a peak in a list of unsorted integers

def find_peak(list_of_integers):
    """
    finds peak func
    """

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]

    mid_index_num = int(len(list_of_integers) / 2)

    if mid_index_num != len(list_of_integers) - 1:
        if list_of_integers[mid_index_num - 1] < list_of_integers[mid_index_num] and\
           list_of_integers[mid_index_num + 1] < list_of_integers[mid_index_num]:
            return list_of_integers[mid_index_num]
    else:
        if list_of_integers[mid_index_num - 1] < list_of_integers[mid_index_num]:
            return list_of_integers[mid_index_num]
        else:
            return list_of_integers[mid_index_num - 1]

    if list_of_integers[mid_index_num - 1] > list_of_integers[mid_index_num]:
        list_nums = list_of_integers[0:mid_index_num]
    else:
        list_nums = list_of_integers[mid_index_num + 1:]

    return find_peak(list_nums)
