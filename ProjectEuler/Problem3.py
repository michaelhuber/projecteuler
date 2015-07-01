#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?
import math

number = 600851475143
endpoint = int(math.sqrt(number)) + 1
lowdivisorlist = []
highdivisorlist = []
possibleprime = 3
primelist = [2]
primedivisorlist = []
allfailed = True

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

"""checkuntil = (divisorlist[-1])/2

while possibleprime < checkuntil:
    for prime in primelist:
        if possibleprime%prime == 0:
            allfailed = False
    if allfailed == True:
        primelist.append(possibleprime)
    possibleprime = possibleprime + 2
    allfailed = True

for divisor in divisorlist:
    for prime in primelist:
        if divisor%prime == 0:
            allfailed = False
    if allfailed == True:
        primedivisorlist.append(divisor)
    allfailed = True

print primedivisorlist"""