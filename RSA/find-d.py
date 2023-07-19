##to find the decryption key (d):
# d = e mod n 
#program to find decryption key 
phi = 60
e = 17

for x in range(phi):
    val = (x * e) % phi
    if val == 1:
        print(val) 
        print(x)
print(( 57**53) % 77 )