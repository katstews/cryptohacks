#private key (d), used to decrypt ciphertext created with
#the corresponding public key, also used to sign msg
#the private key(d), is the fastest way to break the 
#encryption algorithm, other wise you'd have to factor the
#modulus

#private = n,d ==> c[i]**d % n (to decrypt)
#public = n,e ==> m[i]**e % n (to encrypt)

#the private key (d), is the modular multiplicative inverse
#of the exponent e modulo THE TOTIENT of N

# d*e % phi = 1

from Crypto.Util.number import inverse

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
N = p*q
phi = (p-1) * (q-1)

d = inverse(e,phi) #OR d = 
print(d)

