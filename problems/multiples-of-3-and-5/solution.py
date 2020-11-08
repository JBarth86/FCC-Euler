#!/bin/python3.7

def multiplesOf3and5(number):
    sum = 0
    for x in range(1, number):
        if (x % 3 == 0 or x % 5 == 0):
            sum += x

    print(sum)


multiplesOf3and5(1000)
