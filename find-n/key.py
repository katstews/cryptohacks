from Cryptodome.PublicKey import RSA

f = open("bruce_rsa.pub", "r") 
pubkey = RSA.import_key(f.read())
print(pubkey.n)

