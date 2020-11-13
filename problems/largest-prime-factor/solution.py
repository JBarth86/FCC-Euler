#!/bin/python3.7

def largestPrimeFactor(number):
    factor = 2

    while number >= factor ** 2:

        if number % factor == 0:
            return largestPrimeFactor(number // factor)

        factor += 1

    return number
