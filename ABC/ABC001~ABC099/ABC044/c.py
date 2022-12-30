n, a = map(int, input().split())
x = list(map(int, input().split()))


ans = 0
for m in range(1, n+1):
    dp = [[0]*(m*a + 5) for _ in range(m+5)]
    dp[0][0] = 1
    for p in x:
        for j in range(m, -1, -1):
            for v in range(m*a + 1):
                if j+1 < m+1 and v+p < m*a + 1:
                    dp[j+1][v+p] += dp[j][v]
    ans += dp[m][m*a]
print(ans)
