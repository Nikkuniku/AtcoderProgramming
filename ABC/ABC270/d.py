N, K = map(int, input().split())
a = list(map(int, input().split()))
INF = float('inf')
dp = [[-INF, INF] for _ in range(N+1)]
dp[N][0] = 0
dp[N][1] = 0
for i in range(N, 0, -1):
    for k in range(K):
        if a[k] > i:
            continue
        if i-a[k] >= 0:
            if dp[i][0] != -INF:
                dp[i-a[k]][1] = min(dp[i-a[k]][1], dp[i][0])
            if dp[i][1] != INF:
                dp[i-a[k]][0] = max(dp[i-a[k]][0], dp[i][1]+a[k])
print(max(dp[0]))
