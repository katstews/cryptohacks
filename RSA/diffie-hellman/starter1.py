## find d, the inverse element 
## g * d mod 991 = 1
from Crypto.Util.number import inverse
prime = 991 
g = 209 

x = inverse(g,prime)
print(x)
