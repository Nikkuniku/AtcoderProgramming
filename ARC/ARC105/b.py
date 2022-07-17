from math import gcd
n = int(input())
a = list(map(int, input().split()))

g = 0
for i in range(n):
    g = gcd(g, a[i])
print(g)
