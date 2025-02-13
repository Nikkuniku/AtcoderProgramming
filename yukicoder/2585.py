N = int(input())
MOD = 998244353
ans = N * (N - 1) * (pow(N - 1, N - 1, MOD) - pow(N - 3, N - 2, MOD)) % MOD
print(ans)
