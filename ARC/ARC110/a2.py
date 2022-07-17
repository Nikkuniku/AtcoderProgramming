from math import gcd
n = int(input())
ans = 1


def lcm(a, b):
    return a*b//gcd(a, b)


for i in range(2, n+1):
    ans = lcm(ans, i)
print(ans+1)
