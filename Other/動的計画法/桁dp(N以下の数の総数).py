n = int(input())
s = str(n)
m = len(s)
dp = [[0, 0] for _ in range(m+1)]
dp[0][0] = 1

for i in range(m):
    D = int(s[i])
    for smaller in range(2):
        limit = 10 if smaller else D+1
        for x in range(limit):
            dp[i+1][smaller | (x < D)] += dp[i][smaller]

print(dp)
print(dp[m][0]+dp[m][1])
