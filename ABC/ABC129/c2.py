n, m = map(int, input().split())
dp = [0]*(n+1)
broken = set([int(input()) for _ in range(m)])
dp[0] = 1
MOD = 10**9 + 7
for i in range(1, n+1):
    if i in broken:
        continue
    if i-1 >= 0:
        if dp[i-1] != -1:
            dp[i] += dp[i-1]
    if i-2 >= 0:
        if dp[i-2] != -1:
            dp[i] += dp[i-2]
    dp[i] %= MOD
print(dp[n])
