from Cryptodome.PublicKey import RSA
from binascii import hexlify

with open("2048b-rsa.pem", 'r') as file:
    content = file.read()
key = RSA.importKey(content)
print(key.n)


## openssl x509 -in 2048b-rsa-example.der
## to get pem version and then work with it 