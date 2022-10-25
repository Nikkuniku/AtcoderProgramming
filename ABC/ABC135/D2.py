s = input()
dp = [[0]*13 for _ in range(len(s)+1)]
dp[0][0] = 1
MOD = 1000_000_007

for i in range(len(s)):
    for j in range(13):
        if s[i] == '?':
            for k in range(10):
                dp[i+1][(10*j+k) % 13] += dp[i][j]
                dp[i+1][(10*j+k) % 13] %= MOD
        else:
            dp[i+1][(10*j+int(s[i])) % 13] += dp[i][j]
            dp[i+1][(10*j+int(s[i])) % 13] %= MOD
print(dp[len(s)][5])
