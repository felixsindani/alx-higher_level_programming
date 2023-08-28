#!/usr/bin/python3
# prints the first x elements of a list and only integers

def safe_print_list_integers(my_list=[], x=0):
    x_elements = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            x_elements += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (x_elements)