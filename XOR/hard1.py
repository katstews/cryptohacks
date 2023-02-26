from pwn import xor
# msg ^ secret key = "crypto{" the first 7 characters
# to get *partial secret key* = msg ^ "crypto{"

hexmsg = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
bytemsg = bytes.fromhex(hexmsg)

newlist = []

# for x in bytemsg:
#     x = chr(x)
#     newlist.append(x)
# print("".join(newlist))

newlist = xor(bytemsg[:7],b"crypto{")
newlist = newlist.decode("utf-8") + 'y'
print(newlist)

newmsg = xor(bytemsg,newlist.encode("utf-8"))
print(newmsg)