#given two prime numbers, p and q, find u and v to find
#gcd(p,q) = 1, thus a*u + b*v = 1
import math
a = 26513
b = 32321

if a < b:
    a,b = b,a

r1, r2 = a,b
u,v = 1,0 
up,vp = 0,1 

while r2 > 0:
    #this will find gcd, where r1 is the gcd val 
    q,r = divmod(r1,r2) 
    r1,r2 = r2,r

    u,v = v,u - q * v
    up,vp = vp,up - q * vp
result = a*u + b*up
print(result)


