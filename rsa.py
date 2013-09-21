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
    
#extended euclidian to be corrected                
def extended_gcd(a,b):
    while a%b != 0:
        q = a/b
        x= extended_gcd(b,a%b)
    return x
p = [0,0]
for i in range(0,2):    
    p[i] = random.getrandbits(int(8))
    while Miller_Rabin(p[i],10) != True:
        p[i] = random.getrandbits(8)
n = p[0]*p[1]
totient = (p[0]-1)*(p[1]-1)
for i in range(1,totient): 
    if not totient%i == 0:
        public_enc_key = i
        break
private_dec_key = extended_gcd(totient,public_enc_key)
print private_dec_key



#Initilization of the encryption/decryption process
user_input = ">>>"
print "Enter numeral for encryption:"
plaintext = int(raw_input(user_input))
ciphertext = pow(plaintext,public_enc_key,n)
print "The cipher text is :%d" %ciphertext
decode = pow(ciphertext,private_dec_key,n)
print "Decoded text: %d" %decode




       
    
