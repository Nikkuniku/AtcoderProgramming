a, b, c, d, e, f = map(int, input().split())
MOD = 998244353
a %= MOD
b %= MOD
c %= MOD
d %= MOD
e %= MOD
f %= MOD
ans = (a*b*c)-(d*e*f)
ans %= MOD
print(ans)
