#!/usr/bin/python

def is_prime(number):
    if number <= 1:
        return False
    
    sqrt = number ** number
    for n in range(2, sqrt + 1):
        print(f"{number} % {n}  = {number % n}")
        # if number % n == 0:
        #     return False

    return True


print(is_prime(11))