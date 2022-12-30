N, P = map(int, input().split())
MOD = 998244353
critical = P*pow(100, MOD-2, MOD)
normal = (100-P)*pow(100, MOD-2, MOD)
dp = [0, 1]
dp[1] = 1
for i in range(2, N+1):
    dp.append(dp[-1]*normal + dp[-2]*critical + 1)
    dp[-1] %= MOD
print(dp[N])
