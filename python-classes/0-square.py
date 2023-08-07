#! /usr/bin/python3

class Square:
    """ 
        This class is a demonstration of how 
        classes  and private attributes are 
        created
    """
    def __init__(self, size):
        '''
            A constructor with the single 
            private variable
        '''
        self.__size = size