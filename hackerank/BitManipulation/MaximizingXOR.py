#!/bin/python3

import math
import os
import random
import re
import sys

'''
Given two integers, l and r, find the maximal value of  a xor b , where  and  satisfy the following condition:
l<=a<=b<=r
'''
# Complete the maximizingXor function below.
def maximizingXor(l, r):
    a = l
    b = r

    maximum = -1
    for i in range(a,b+1):
        for j in range(a,i):
            if(i^j > maximum):
                maximum = i^j

    return maximum

if __name__ == '__main__':
    print("Maximizing XOR")
    print("Given two integers, l and r, find the maximal value of  a xor b , where  and  satisfy the following condition:\nl<=a<=b<=r")
    l = input("Enter l: ")
    r = input("Enter r: ")
    result = maximizingXor(l,r)
    print("Result is: " + str(result))
