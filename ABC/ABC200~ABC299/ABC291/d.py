N = int(input())
dp = [[0, 0]*2 for _ in range(N)]
dp[0] = [1, 1]
omote_pre, ura_pre = -1, -1
MOD = 998244353
for i in range(N):
    a, b = map(int, input().split())
    if i == 0:
        omote_pre = a
        ura_pre = b
        continue
    if a != omote_pre:
        dp[i][0] += dp[i-1][0]
    if a != ura_pre:
        dp[i][0] += dp[i-1][1]
    if b != omote_pre:
        dp[i][1] += dp[i-1][0]
    if b != ura_pre:
        dp[i][1] += dp[i-1][1]
    dp[i][0] %= MOD
    dp[i][1] %= MOD
    omote_pre = a
    ura_pre = b
ans = sum(dp[N-1]) % MOD
print(ans)
