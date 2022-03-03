
from distutils.command.build_scripts import first_line_re
import re


def countdown(firstNum):
    if firstNum <= 0:
        print("Please give me a positive number to countdown from")
    for i in range(firstNum, 0, -1):
        print(i)

countdown(10)

def recursiveCountdown(firstNum):
    if firstNum <= 0:
        return 1
    print(firstNum)
    return recursiveCountdown(firstNum-1)

recursiveCountdown(10)

##Write a funciton that will return the sum of all numbers from zero up to a given integer

def sumNumbers(givenInteger):
    sumTotal = 0
    for i in range(1, givenInteger+1, 1):
        sumTotal+= i
    return sumTotal

print(sumNumbers(4))

def recursiveSum(givenInteger):
    if givenInteger<=0:
        return 0
    return givenInteger + recursiveSum(givenInteger-1)

print(recursiveSum(5))

## 1   2   3   4   5   6
## 1 + 1 + 2 + 3 + 5 + 8
# Write a function that returns the value of a certain fibonacci sequenced position

def recursiveFib(int):
    if int == 1 or int == 2:
        return 1
    return recursiveFib(int - 1) + recursiveFib(int - 2)

print(recursiveFib(15))