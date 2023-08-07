#! /usr/bin/python3
"""
    Class demonstration to test for 
    assertion of variable types
"""

class Square:
    """
        Square classes
    """
    def __init__(self, size=0):
        if not type(size) == int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
    