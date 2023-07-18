#! /usr/bin/python3

def fibonacci_sequence(n):
    first, second = 0 , 1
    print("{}\n{}".format(first, second))
    for _ in range(1, n):
        first, second = second, (first + second)
        print("{}".format(second), end="\n")