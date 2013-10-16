


#returns a number c such that d*a + c*b = gcd(a,b) for some d
def extended_gcd(a,b):
    aux1 = 0
    aux2 = 1
    n = a
    while b != 0:
        q = a / b
        r = a % b
        a = b
        b = r
        temp = aux2
        aux2 = aux1-q*aux2
        aux1 = temp
    if temp < 0:
        temp = n + temp
    return temp

def gcd(m, n):
    while n > 0:
    	temp = n
    	n = m % n
    	m = temp
    return m

# needs to be fixed
def get_comprime( number ):
    for i in range(2,int( number**0.5 )):
        if gcd( number, i ) == 1:
        	   return i 
        	     
