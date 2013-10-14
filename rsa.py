#! /usr/local/bin/python
import random
import sys

def Miller_Rabin(n, k=100):
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

def get_comprime( number ):
    for i in range(2,int( number**0.5 )):
        if gcd( number, i ) == 1:
        	   return i 
        	     
def init_rsa( millerab_par, bitlength ):    
    p = [0, 0]
    for i in range(0, 2):    
        p[i] = random.getrandbits( int( bitlength ))
        while Miller_Rabin( p[i], millerab_par ) != True:
            p[i] = random.getrandbits( bitlength )
   


    modulus = p[0]*p[1]
    totient = ( p[0]-1 )*( p[1]-1 )
    public_enc_key = get_comprime( totient )
    private_dec_key = extended_gcd(totient,
                                   public_enc_key)
    return modulus, public_enc_key, private_dec_key
                               
if __name__ == "__main__":
    import sys
    keylength = 16 
    pseudoprime, public_key, private_key = init_rsa( int( sys.argv[1]),
                                                            keylength) 
    print pseudoprime
    print public_key
    print private_key



    user_input = ">>>"
    plaintext = int( raw_input( user_input ))
    print "Enter numeral for encryption:"
    
    while plaintext > pseudoprime:
        print "Invalid message length.Please try a shorter numeral"
        print "Enter numeral for encryption:"
        plaintext = int( raw_input( user_input ))
    ciphertext = pow(plaintext,
                     public_key, pseudoprime)
    print "The cipher text is :%d" %ciphertext
    decode = pow( ciphertext, 
             private_key, pseudoprime ) 
    print "Decoded text: %d" %decode
