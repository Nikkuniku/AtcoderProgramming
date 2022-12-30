n = input()
m = len(n)

dp = [[[0]*12 for _ in range(2)] for _ in range(m+1)]
dp[0][0][0] = 1
for i in range(m):
    for smaller in range(2):
        limit = 10 if smaller else int(n[i])+1
        for j in range(10):
            for x in range(limit):
                dp[i+1][smaller | (x < int(n[i]))][j +
                                                   (1 if x == 1 else 0)] += dp[i][smaller][j]
ans = 0
for i in range(11):
    ans += i*dp[m][0][i]
    ans += i*dp[m][1][i]
print(ans)
