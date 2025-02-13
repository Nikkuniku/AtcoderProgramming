from collections import defaultdict

H, W = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(H)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
d = defaultdict(int)
dp = [[1 << 60, -(1 << 60)] for _ in range(H * W)]
for i in range(H):
    for j in range(W):
        m = M[i][j]
        d[m - 1] = (i, j)
        isok = True
        for dx, dy in dxy:
            ni = i + dx
            nj = j + dy
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if m >= M[ni][nj]:
                isok = False
        if isok:
            dp[m - 1][0] = m - 1
            dp[m - 1][1] = m - 1

for v in range(H * W):
    i, j = d[v]
    for dx, dy in dxy:
        ni = i + dx
        nj = j + dy
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        to = M[ni][nj] - 1
        if v < to:
            dp[to][0] = min(dp[to][0], dp[v][0])
            dp[to][1] = max(dp[to][1], dp[v][1])
ans = 0
for i in range(H * W):
    ans += dp[i][0] != dp[i][1]
print(ans)
