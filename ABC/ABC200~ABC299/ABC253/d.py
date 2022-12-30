from math import gcd
n, a, b = map(int, input().split())
c = (a*b)//gcd(a, b)


def tosa(a, d, n):
    return n*(2*a + (n-1)*d)//2


i = n//a
j = n//b
k = n//c
sa = tosa(a, a, i)
sb = tosa(b, b, j)
sc = tosa(c, c, k)
s = n*(n+1)//2
ans = s-sa-sb+sc
print(ans)
