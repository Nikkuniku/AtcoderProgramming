n = int(input())
s = str(n)
m = len(s)
dp = [[[0]*2 for _ in range(2)] for _ in range(m+1)]
dp[0][0][0] = 1

for i in range(m):
    D = int(s[i])
    for smaller in range(2):
        limit = 10 if smaller else D+1
        for j in range(2):
            for x in range(limit):
                dp[i+1][smaller | (x < D)][j | (x == 3)] += dp[i][smaller][j]

print(dp)
print(dp[m][0][1]+dp[m][1][1])
