#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True: if it is an instance of the given class.
        False: Otherwise.
    """
    return True if type(obj) is a_class else False
