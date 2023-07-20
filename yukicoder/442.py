from math import gcd
A, B = map(int, input().split())
g = gcd(A, B)
a = A//g
b = B//g
ans = g*gcd(a+b, g)
print(ans)
