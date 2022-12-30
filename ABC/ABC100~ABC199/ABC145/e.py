N, T = map(int, input().split())
cook = [tuple(map(int, input().split())) for _ in range(N)]
ab = [cook[i][0] for i in range(N)]
cook.sort(key=lambda x: x[0])
amax = max(ab)
dp = [[0]*(T+amax+1) for _ in range(N+1)]
for i in range(N):
    a, b = cook[i]
    for t in range(T+amax+1):
        dp[i+1][t] = max(dp[i+1][t], dp[i][t])
        if 0 <= t-a < T:
            dp[i+1][t] = max(dp[i+1][t], dp[i][t-a]+b)

ans = 0
for j in range(T+amax+1):
    ans = max(ans, dp[N][j])
print(ans)
