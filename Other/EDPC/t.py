n = int(input())
s = '0'+input()
MOD = 1_000_000_007
dp = [[0]*(n+1) for _ in range(n+1)]

# 初期値
for j in range(n):
    dp[1][j] = 1

for i in range(2, n+1):
    # 累積和
    cum = [0]
    for j in range(n):
        cum.append(cum[-1]+dp[i-1][j])

    if s[i-1] == '>':
        for j in range(n-i+1):
            dp[i][j] += cum[j+1]
            dp[i][j] %= MOD
    else:
        for j in range(n-i+1):
            dp[i][j] += cum[n-i+2]-cum[j+1]
            dp[i][j] %= MOD

ans = dp[n][0] % MOD
print(ans)
