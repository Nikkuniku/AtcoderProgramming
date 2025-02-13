N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (1 << N)
for s in range(1 << N):
    for i in range(N):
        for j in range(i + 1, N):
            if s & (1 << i) and s & (1 << j):
                dp[s] += A[i][j]
for s in range(1 << N):
    t = s
    while t > 0:
        t = (t - 1) & s
        dp[s] = max(dp[s], dp[s ^ t] + dp[t])
print(dp[-1])
