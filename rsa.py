#!/usr/local/bin/python

import random
import sys
from modules import millerabin, euclid

      	     

#---------------Calculates all the pretty stuff------------------------------

def init_rsa( keylength ):
    
    p = [0, 0]
    for i in range(0, 2):    
        p[i] = random.getrandbits( int( keylength ))

        while millerabin.isprime( p[i] ) != True:
            p[i] = random.getrandbits( keylength )


    modulus = p[0] * p[1]
    totient = ( p[0]-1 ) * ( p[1]-1 )


    public_enc_key = euclid.get_comprime( totient )
    private_dec_key = euclid.extended_gcd(totient,
                                   public_enc_key)
    
    return modulus, public_enc_key, private_dec_key



#---------Reads from stdin the keylength and starts the generation process-----

if __name__ == "__main__":
   
    import sys
    keylength =int( sys.argv[1])
    pseudoprime, public_key, private_key = init_rsa( keylength ) 
    

    print pseudoprime
    print public_key
    print private_key


    user_input = ">>>"
    plaintext = int( raw_input( user_input ) )
    print "Enter numeral for encryption:"
    
    while plaintext > pseudoprime:
        print "Invalid message length.Please try a shorter numeral"
        print "Enter numeral for encryption:"
        plaintext = int( raw_input( user_input ) )
   

	
    ciphertext = pow( plaintext,
                      public_key,
                      pseudoprime)

    print "The cipher text is :%d" %ciphertext
   

    decode = pow( ciphertext, 
                  private_key, 
                  pseudoprime ) 
   

    print "Decoded text: %d" %decode
