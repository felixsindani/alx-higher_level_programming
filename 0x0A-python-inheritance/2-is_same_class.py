#!/usr/bin/python3
"""Defines a class comparing function"""

def is_same_class(obj, a_class):
    """Check if an object is exactly an instance(same) as of given class

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to
    Returns:
        True if the object is exactly an instance of the specified class ; otherwise False
    """
    if type(obj) == a_class:
        return True
    return False