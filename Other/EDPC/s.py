d = int(input())
k = input()
n = len(k)

dp = [[[0]*d for _ in range(2)] for _ in range(n+1)]
dp[0][0][0] = 1
MOD = 1000000007
for i in range(n):
    p = int(k[i])
    for smaller in range(2):
        limit = 10 if smaller else p+1
        for m in range(d):
            for x in range(limit):
                dp[i+1][smaller | (x < p)][(m+x) % d] += dp[i][smaller][m]
                dp[i+1][smaller | (x < p)][(m+x) % d] %= MOD

print((dp[n][0][0]+dp[n][1][0]-1) % MOD)
