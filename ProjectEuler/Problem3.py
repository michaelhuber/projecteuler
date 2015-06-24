#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

number = 39
divisor = 3
primelist = [3]
primedivisorlist = []

while (divisor < number/2):
    for i in primelist:
        if divisor%i != 0:
            primelist.append(divisor)
            break
    divisor = divisor + 2

for i in primelist:
    if number%i == 0:
        primedivisorlist.append(i)
    
print primelist