N, T = map(int, input().split())
cook = [tuple(map(int, input().split())) for _ in range(N)]
cook.sort(key=lambda x: x[0])
cook.sort(key=lambda x: x[1])
X = cook.pop()

dp = [[0]*T for _ in range(N)]
for i in range(N-1):
    a, b = cook[i]
    for t in range(T):
        dp[i+1][t] = max(dp[i+1][t], dp[i][t])
        if t-a >= 0:
            dp[i+1][t] = max(dp[i+1][t], dp[i][t-a]+b)

ans = dp[N-1][T-1]+X[1]
print(*dp, sep="\n")
print(ans)
