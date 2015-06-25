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


for i in range(2, endpoint):
    if number%i == 0:
        lowdivisorlist.append(i)
        
for i in lowdivisorlist:
    highdivisorlist.append(number/i)

divisorlist = lowdivisorlist + highdivisorlist
divisorlist.sort()
#print "The divisors of " + str(number) + " are " + str(divisorlist)

while possibleprime < endpoint:
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

print primedivisorlist

"""while divisor < math.sqrt(number):
    for i in primelist:
        if divisor%i == 0:
            allfailed == False
            break  
    if allfailed == True:
        primelist.append(divisor)
    divisor = divisor + 2

for i in primelist:
    if number%i == 0:
        primedivisorlist.append(i)
    
importantprime = primedivisorlist[-1]
answer = number/importantprime
print primelist
print answer
print importantprime"""
