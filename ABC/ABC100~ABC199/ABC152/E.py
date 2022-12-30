from math import gcd
N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7


def lcm(a, b):
    return a*b//(gcd(a, b))


def inv(b):
    return pow(b, MOD-2, MOD)


L = 1
for a in A:
    L = lcm(L, a)

ans = 0
for a in A:
    ans += L*inv(a)
    ans %= MOD
print(ans)
