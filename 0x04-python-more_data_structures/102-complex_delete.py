#!/usr/bin/python3
# function that deletes keys with
# a specific value in a dictionary.
def complex_delete(a_dictionary, value):
    list_of_keys = list(a_dictionary.keys())
    for i in list_of_keys:
        if value == a_dictionary.get(i):
            del a_dictionary[i]

    return (a_dictionary)
