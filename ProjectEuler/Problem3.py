#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

number = 600851475143
divisor = (number - 1) / 2
factorlist = []
def step(start, end , step):
    while start <= end:
        yield start
        start = start - step
    
divisor.step((number - 1)/2, 1, 2)

#while (divisor > 0):
#    if number%divisor == 0:
#        factorlist.append(divisor)
#    divisor = divisor - 2
#print factorlist
    
    
