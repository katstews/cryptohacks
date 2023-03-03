#brute force this btich
g = 3 
m = 13
d = 0 #this will be the special inverse val

for x in range(13): 
    if ((3*x) % m)  == 1:
       d = x
print(d)