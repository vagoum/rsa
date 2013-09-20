import random,sys

def Miller_Rabin(n,k):
    d = n-1
    s = 0
    while d % 2 == 0:
        d = d/2
        s += 1
    for i in xrange(k):
        a = random.randrange(n)
        return validation(a,d,n,s)
        if not validation:
            return False
    return True
    
def validation(a,d,n,s):
    power = pow(a,d,n)
    if power == 1:
        return True
    for i in xrange(s-1):
        if power == n-1 :
           return True
        power = pow(power,2,n)
    return (power == n-1)
    
                
def extended_gcd(k,l):
    if l == 0 :
        return 1
    else:
        q = k/l
        r = k%l
        (x,y) = extended_gcd(b,r)
    return x
    
par = argv[2]
bitlength = argv[1]
p = [0,0]
for i in range(0,2):     #generation of 2 64-bit prime numbers
    p[i] = random.getrandbits(int(bitlength))
    while Miller_Rabin(p[i],par) != True:
        p[i] = random.getrandbits(64)

n = p[0]*p[1]
totient = (p[0]-1)*(p[1]-1)
for i in xrange(totient): 
    if not totient%i == 0:
        public_enc_key = i
        break
private_dec_key = extended_gcd(public_enc_key,totient)
"""print "Enter numeral for encryption:"
plaintext = raw_input(user)
ciphertext = pow(plaitext,public_enc_key,n)
print "The cipher text is :%d" %ciphertext
decode = pow(ciphertext,private_dec_key,n)
print "Decoded: %d" %decode"""


       
    