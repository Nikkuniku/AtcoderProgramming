from math import gcd
N = int(input())
A = list(map(int, input().split()))
L = 1
for a in A:
    L = L*a//gcd(L, a)
print(L)
