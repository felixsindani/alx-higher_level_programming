#!/usr/bin/python3
# returns: real number of elements printed

def safe_print_list(my_list=[], x=0):
    real_nu_elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            real_nu_elements += 1
        except IndexError:
            break
    print("")
    return (real_nu_elements)