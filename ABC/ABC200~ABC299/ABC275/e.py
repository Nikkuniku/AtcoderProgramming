

def inv(b):
    return pow(b, MOD-2, MOD)


N, M, K = map(int, input().split())
MOD = 998244353
dp = [0]*(N+1)
dp[0] = 1
q = inv(M)
for _ in range(K):
    dp1 = [0]*(N+1)
    for i in range(N+1):
        if i == N:
            dp1[i] += dp[i]
            dp1[i] %= MOD
        else:
            for j in range(1, M+1):
                if i+j <= N:
                    dp1[i+j] += dp[i]*q
                    dp1[i+j] %= MOD
                else:
                    p = N-(i+j-N)
                    dp1[p] += dp[i]*q
                    dp1[p] %= MOD

    dp, dp1 = dp1, dp
print(dp[N] % MOD)
