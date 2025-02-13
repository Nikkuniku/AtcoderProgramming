H, W, Y = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
Q = [[] for _ in range(Y + 1)]
isSeen = [[False] * W for _ in range(H)]
dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]
for i in range(H):
    for j in range(W):
        if i == 0 or i == H - 1 or j == 0 or j == W - 1:
            if A[i][j] <= Y:
                Q[A[i][j]].append((i, j))
                isSeen[i][j] = True

for k in range(Y + 1):
    if not Q[k]:
        continue
    i = 0
    while i < len(Q[k]):
        vi, vj = Q[k][i]
        for dx, dy in dxy:
            ni = vi + dx
            nj = vj + dy
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if isSeen[ni][nj]:
                continue
            if k < A[ni][nj] <= Y:
                Q[A[ni][nj]].append((ni, nj))
                isSeen[ni][nj] = True
            elif A[ni][nj] <= k:
                Q[k].append((ni, nj))
                isSeen[ni][nj] = True
        i += 1
ans = H * W
for k in range(1, Y + 1):
    ans -= len(Q[k])
    print(ans)
