A, B, C, D, E, F = map(int, input().split())
MOD = 998244353
A %= MOD
B %= MOD
C %= MOD
D %= MOD
E %= MOD
F %= MOD
ans = ((A * B * C) % MOD - (D * E * F) % MOD) % MOD
print(ans)
