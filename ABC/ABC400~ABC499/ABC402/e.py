N, X = map(int, input().split())
Problems = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (X + 1) for _ in range(1 << N)]
for s in range((1 << N) - 1, -1, -1):
    for c in range(X, -1, -1):
        for i in range(N):
            S, C, P = Problems[i]
            if s & (1 << i):
                continue
            if c + C <= X:
                dp[s][c] = max(
                    dp[s][c],
                    (dp[s | (1 << i)][c + C] + S) * P / 100
                    + (dp[s][c + C]) * (100 - P) / 100,
                )
ans = dp[0][0]
print(ans)
