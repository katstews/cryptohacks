from Cryptodome.PublicKey import RSA

with open('privacy_enhanced_mail.pem', 'r') as file:
    content = file.read()

key = RSA.importKey(content)
print(key.d)
