#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindrome made from the product of two 3-digit numbers.
import math

number = 998001
endpoint = int(math.sqrt(number)) + 1
lowdivisorlist = []
highdivisorlist = []

def factor(input):
    endpoint = int(math.sqrt(number)) + 1
    lowdivisorlist = []
    highdivisorlist = []

    for i in range(2, endpoint):
        if input%i == 0:
            lowdivisorlist.append(i)
                
    for i in lowdivisorlist:
        highdivisorlist.append(number/i)

    divisorlist = lowdivisorlist + highdivisorlist
    divisorlist.sort()
    print divisorlist

factor(number)