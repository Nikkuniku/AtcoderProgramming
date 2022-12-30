s = input()
s = s[::-1]
dp = [[0]*13 for _ in range(len(s)+1)]
dp[0][0] = 1
pows = []
MOD = 1000_000_007
for i in range(len(s)+1):
    pows.append(pow(10, i, 13))
for i in range(len(s)):
    if s[i] == '?':
        for j in range(13):
            for k in range(10):
                k = (k*pows[i]) % 13
                dp[i+1][(j+k) % 13] += dp[i][j]
                dp[i+1][(j+k) % 13] %= MOD
    else:
        v = int(s[i])*pows[i] % 13
        for j in range(13):
            dp[i+1][(v+j) % 13] += dp[i][j]
            dp[i+1][(v+j) % 13] %= MOD

print(dp[len(s)][5])
