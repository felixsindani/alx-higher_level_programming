#!/usr/bin/python3
# divides element by element 2 lists
# If an element is not an integer or float:
# print: wrong type
# If the division can’t be done (/0):
# print: division by 0
# If my_list_1 or my_list_2 is too short
# print: out of range

def list_division(my_list_1, my_list_2, list_length):
    NewList_formed = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            NewList_formed.append(div)
    return (NewList_formed)