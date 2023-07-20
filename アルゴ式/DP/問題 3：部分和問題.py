N, M = map(int, input().split())
A = list(map(int, input().split()))
dp = [[False]*(M+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    for s in range(M+1):
        dp[i+1][s] |= dp[i][s]
        if s-A[i] >= 0:
            dp[i+1][s] |= dp[i][s-A[i]]
ans = 'Yes' if dp[N][M] else 'No'
print(ans)
