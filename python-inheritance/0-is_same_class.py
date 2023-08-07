#! /usr/bin/python3
"""
    Module documentation goes here
"""
def is_same_class(obj, a_class):
    """Function documentation goes here"""
    if type(obj) == bool or obj == None:
        isbool = False
    elif isinstance(obj, a_class):
        isbool = True
    
    return isbool