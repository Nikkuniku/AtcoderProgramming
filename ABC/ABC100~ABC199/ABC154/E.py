n = input()
m = len(n)
k = int(input())

dp = [[[0, 0, 0, 0, 0] for _ in range(2)] for _ in range(m+1)]
dp[0][0][0] = 1

for i in range(m):
    for smaller in range(2):
        lim = 10 if smaller else int(n[i])+1
        for j in range(4):
            for x in range(lim):
                dp[i+1][smaller | (x < int(n[i]))][j +
                                                   (1 if x != 0 else 0)] += dp[i][smaller][j]

ans = dp[m][0][k]+dp[m][1][k]
print(ans)
