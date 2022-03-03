#Recursive Fibonacci
from turtle import rt


def RFib(num):
    if num <= 2:
        return 1
    return RFib(num-1) + RFib(num-2)

print(RFib(7))


#Recursive Tribonacci

def RTrib(num):
    if num == 3 or num == 2:
        return 1
    elif num < 2:
        return 0
    return RTrib(num-1) + RTrib(num-2) + RTrib(num-3)

print(RTrib(6))

#Paging Dr. Ackermann

