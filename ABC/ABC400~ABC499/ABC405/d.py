from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
ans = [[-1] * W for _ in range(H)]
q = deque()
dxy = [(0, 1, "<"), (0, -1, ">"), (-1, 0, "v"), (1, 0, "^")]
for i in range(H):
    for j in range(W):
        if S[i][j] == "E":
            q.append((i, j))
            ans[i][j] = "E"

while q:
    vi, vj = q.popleft()
    for di, dj, route in dxy:
        ni = vi + di
        nj = vj + dj
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if S[ni][nj] != ".":
            continue
        if ans[ni][nj] == -1:
            ans[ni][nj] = route
            q.append((ni, nj))
for i in range(H):
    for j in range(W):
        if ans[i][j] == -1:
            ans[i][j] = "#"
for c in ans:
    print(*c, sep="")
