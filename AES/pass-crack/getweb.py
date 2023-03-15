import requests 
from Crypto.Cipher import AES
import hashlib
import random

ciphertexthex = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

with open("words.txt", 'r') as f:
    for word in f:
        word = word.strip()
        key1 = hashlib.md5(word.encode()).digest()
        key = bytes(key1)
        cipher = AES.new(key,AES.MODE_ECB)
        ciphertext = bytes.fromhex(ciphertexthex)
        decrypted = cipher.decrypt(ciphertext)
        if b'crypto{' in decrypted:
            print(decrypted)
        