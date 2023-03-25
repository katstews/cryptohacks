#find the Euler Totent(phi), if p & q are found, of N
#phi = (p-1) * (q-1), phi will help decrypt ciphertext
p = 857504083339712752489993810777
q = 1029224947942998075080348647219

N = p * q
phi = (p-1) * (q-1)
print(phi)