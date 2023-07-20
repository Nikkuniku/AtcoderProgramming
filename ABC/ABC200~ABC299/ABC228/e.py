from math import gcd
N, K, M = map(int, input().split())
MOD = 998244353
g = gcd(MOD, M)
ans = 0
if g == 1:
    ans = pow(M, pow(K, N, MOD-1), MOD)
print(ans)
