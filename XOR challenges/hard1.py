from Cryptodome.Util.number import * 
# from pwn import xor
# msg ^ secret key = "crypto{" the first 7 characters
# to get *partial secret key* = msg ^ "crypto{"
# need to run on kali since m1 doesnt supp pwntools

hexmsg = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
bytemsg = bytes.fromhex(hexmsg)

flag = b""

newlist = []

contain = b"crypto{"
val = bytemsg[:7]

key = long_to_bytes(bytes_to_long(contain)^bytes_to_long(val))
key = key + b'y'

for x in range(0,len(hexmsg),2):
    val = hexmsg[x:x+2]
    newlist.append(bytes.fromhex(val))
        
for i,x in enumerate(newlist):
    keyval = key[i % len(key)]
    val1 = keyval ^ bytes_to_long(x)
    flag += long_to_bytes(val1)
    
print(flag)

