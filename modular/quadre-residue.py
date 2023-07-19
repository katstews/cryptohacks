#modular square root
#why is this so hard? 
# i just need to study lmao

ints = [14,6,11]
p = 29

vals = []

for x in range(1,p):
    val = (x**2) % p
    ## found that 6 is the quadratic residue of the list of ints BRUH
    ## there will be two 6's as quadratic residues are symmetric 
    if val == 6:
        print(x)
    vals.append(val) 

## shortcut to find quadratic residue 
for x in ints:
    val = pow(x, (28)//2, 29)
    print(val)