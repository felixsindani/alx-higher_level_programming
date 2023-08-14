#!/usr/bin/python3
# unction that removes all characters c and C from a string
# 5-no_c.py

def no_c(my_string):
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))
