#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

number = 600851475143
divisor = 3
primelist = [3, 5, ]
primedivisorlist = []

while (divisor < number/2):
    for i in primelist:
        if divisor%i == 0:
            break
    else:
        primelist.append(divisor)
    divisor = divisor + 2

for i in primelist:
    if number%i == 0:
        primedivisorlist.append(i)
    
print primedivisorlist[-1]