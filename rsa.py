import random,sys


def Miller_Rabin(n,k):
    if n % 2 == 0:
        return False
    s = 0
    d = n-1
    while d % 2 == 0:
        d = d/2
        s += 1
    assert(2**s*d == n-1)
    for i in xrange(k):
        a = random.randrange(2,n)
        return validation(a,d,n,s)
        if not validation:
            return False
    return True

def validation(a,d,n,s):
    power = pow(a,d,n)
    if power == 1:
        return True
    for i in  xrange(s-1):
        if power == n-1:
           return True
        power = pow(power,2,n)
    return (power == n-1)
              
def extended_gcd(a,b):
    aux1 = 0
    aux2 = 1
    n = a
    while b != 0:
        q = a/b
        r = a%b
        a = b
        b = r
        temp = aux2
        aux2 = aux1-q*aux2
        aux1 = temp
    if temp < 0:
        temp = n + temp
    return temp

def gcd(m,n):
    while n > 0:
    	temp = n
    	n = m%n
    	m = temp
    return m
    
    
p = [0, 0]
for i in range(0, 2):    
    p[i] = random.getrandbits(int(26))
    while Miller_Rabin(p[i],100) != True:
        p[i] = random.getrandbits(26)
modulus = p[0]*p[1]
totient = (p[0]-1)*(p[1]-1)
for i in range(2,int(totient**0.5)): 
    if gcd(totient, i) == 1:
        public_enc_key = i
        break
private_dec_key = extended_gcd(totient,
                               public_enc_key)

print modulus
print public_enc_key
print private_dec_key
#Initilization of the encryption/decryption process

user_input = ">>>"
plaintext = int(raw_input(user_input))
print "Enter numeral for encryption:"
while plaintext > modulus:
    print "Invalid message length.Please try a shorter numeral"
    print "Enter numeral for encryption:"
    plaintext = int(raw_input(user_input))
ciphertext = pow(plaintext,
                 public_enc_key, modulus)
print "The cipher text is :%d" %ciphertext
decode = pow(ciphertext, 
             private_dec_key, modulus)
print "Decoded text: %d" %decode




       
    
