#! /usr/bin/python3
"""
    Module documentation goes here
"""
def is_same_class(obj, a_class):
    """Function documentation goes here"""
    if type(obj) == bool or obj == None or isinstance(repr(obj), a_class):
        return False
    
    return isinstance(obj, a_class)
