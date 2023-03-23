#RSA encryption is modular exponentiation of a message
#with an exponent (e) and an modulus (N), N = p*q (two prime #)
#Together they form a RSA public key, (N,e)
#Most common value for e is 0x1001 or 65537

e = 65537
N = 17 * 23 

#you could this do this but no one does this...
        #key = (12**e) % N
#instead use pow, pow(number,power,modulus(optional))
key = pow(12,e,N)
print(key)