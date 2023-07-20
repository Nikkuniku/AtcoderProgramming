from random import randint
from math import gcd
a = []
A = randint(1, 100)
M = randint(1, 100)
g = gcd(A, M)
for i in range(100):
    a.append(pow(A, i, M))
print(a)
print(g)
