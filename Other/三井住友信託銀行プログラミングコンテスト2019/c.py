X = int(input())
W = [i for i in range(100, 106)]
N = len(W)
dp = [[False] * (X + 1) for _ in range(N + 1)]
dp[0][0] = True
for i in range(N):
    p = W[i]
    for w in range(X + 1):
        dp[i + 1][w] |= dp[i][w]
        if w - p >= 0:
            dp[i + 1][w] |= dp[i][w - p]
            dp[i + 1][w] |= dp[i + 1][w - p]
ans = 1 if dp[N][X] else 0
print(ans)
