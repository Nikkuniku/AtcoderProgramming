N = int(input())
MOD = 998244353
M = len(str(N))
p = pow(10, M, MOD)
inv = pow(p - 1, -1, MOD)
ans = (pow(10, N * M, MOD) - 1) * N * inv % MOD
print(ans)
