N, P = map(int, input().split())
MOD = 998244353


def inv(k):
    return pow(k, MOD-2, MOD)


dp = [0]*(N+1)
dp[1] = 1
for i in range(N, -1, -1):
    if i+2 <= N:
        dp[i] += P*inv(100)*(dp[i+2]+1)
    if i+1 <= N:
        dp[i] += (100-P)*inv(100)*(dp[i+1]+1)
    dp[i] %= MOD

print(dp[1] % MOD)
