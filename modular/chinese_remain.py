## when two numbers are coprime, that means they only share 1 as their prime
import sys

"""
In cryptography, we commonly use the Chinese Remainder Theorem to 
help us reduce a problem of very large integers into a set of several,
easier problems.

This will only work because all moduli all do NOT share any common factors. 

x = 2 mod 5  *5
x = 3 mod 11 *3
x = 5 mod 17 *5

"""

values = [[2,5],[3,11],[5,17]]
b = [2,3,5]
N = 5 * 11 * 17
n = [187, 85, 55]
x = [3,7,13]
remainder = [2, 8, 4]
final_val = [1122, 1785, 3575]

val = sum(final_val)
y = val % N 

print(y % 5)
print(y % 11)
print(y % 17)



# for p in range(3):
#     y = b[p] * n[p] * x[p]
#     final_val.append(y)
# print(final_val)


## find x 
# a = 0
# for y in remainder:
#     for z in range(20):
#         if ((y*z) % values[a][1]) == 1:
#             x.append(z)
#             break
#     a += 1 
# print(x)

#find remainder 
# print((5 * 37) % 187)
# print((11 * 7) % 85)
# print((17 * 3) % 55)