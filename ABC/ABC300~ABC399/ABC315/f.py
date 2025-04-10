def dist(px, py, qx, qy):
    return ((px - qx) ** 2 + (py - qy) ** 2) ** 0.5


def cost(c):
    if c > 0:
        return pow(2, c - 1)
    else:
        return 0


N = int(input())
C = 30
INF = 1 << 60
Points = [list(map(int, input().split())) for _ in range(N)]
dp = [[INF] * (C + 1) for _ in range(N + 1)]
dp[1][0] = 0
for i in range(1, N):
    for c in range(C + 1):
        for k in range(1, C + 1):
            if i + 1 - k >= 0 and c - (k - 1) >= 0:
                dp[i + 1][c] = min(
                    dp[i + 1][c],
                    dp[i + 1 - k][c - (k - 1)]
                    + dist(*Points[i], *Points[i - k])
                    + cost(c)
                    - cost(c - (k - 1)),
                )
ans = min(dp[N])
print(ans)
