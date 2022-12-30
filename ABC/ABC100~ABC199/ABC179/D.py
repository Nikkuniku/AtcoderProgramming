n, k = map(int, input().split())

dp = [0]*(n+1)
dp[1] = 1
MOD = 998244353
S = []
for _ in range(k):
    S.append(tuple(map(int, input().split())))

for i in range(2, n+1):
    for j in range(k):
        l, r = S[j]
        dp[i] += dp[max(0, i-l)]-dp[max(0, i-(r+1))]
    dp[i] += dp[i-1]
    dp[i] %= MOD

ans = (dp[n]-dp[n-1]) % MOD
print(ans)
