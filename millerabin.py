
"""
An implementation of the probabilistic Miller_Rabin Algorithm
for primality testing.Given a parameter k,the algorithm gets the
correct result 1 - (1/4)^k of the times.Returns False when number 
is definitely composite and True when number is probably prime.

"""


import random

def isprime(n, k=100):
    if n % 2 == 0 or n % 3 == 0:
        return False
    s = 0
    d =  n-1
    while d % 2 == 0:
        d = d / 2
        s += 1
    for i in xrange(k):
        a = random.randrange(2, n-1)
        if not validation(a, d, n, s):
            return False
    return True

def validation(a, d, n, s):
    power = pow(a, d, n)
    if power == 1:
        return True
    for i in  xrange(s-1):
        if power == n-1:
           return True
        power = pow(power, 2, n)
    return (power == n-1)
              

