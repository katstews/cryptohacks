#find the gcd of two given integers 
#a = b*quotient + remainder
#gcd(a,b) = gcd(b,r)
#use of Euclid algorithm 
import math
a = 66528
b = 52920

q = 0
r = 0
gcd = 0

while(a and b != 0):
    q = math.floor(a/b)
    r = a % b 
    a = b 
    b = r
    if a == 0:
        gcd = b
    elif b == 0:
        gcd = a 
    print(a,b)
print(gcd)