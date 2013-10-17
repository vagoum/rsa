
def gcd(m, n):
    while n > 0:
    	temp = n
    	n = m % n
    	m = temp
    return m

#------assumes that the parameter is a composite number-----------------------

maxprime = 0
def gimmekey( number ):
    for i in range(2,int( number**0.5 )):
        if gcd( number, i ) == 1:
        	   maxprime = i

    return maxprime        	     
