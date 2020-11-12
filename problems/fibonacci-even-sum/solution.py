#!/bin/python3.7

def fiboEvenSum(n):
    a = 1
    b = 1
    c = a + b
    sum = 0

    while c <= n:
        sum += c if c % 2 == 0 else 0

        a = b
        b = c
        c = a + b

    return sum
