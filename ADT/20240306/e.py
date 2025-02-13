H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]


def solve(i, j):
    if S[i][j] == "#":
        return 0
    dxy = [(1, 1), (1, 0), (1, -1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
    cnt = 0
    for dx, dy in [(1, 0), (1, -1), (0, -1)]:
        ni = i + dx
        nj = j + dy
        if 0 <= ni < H and 0 <= nj < W:
            if S[ni][nj] == "#":
                cnt += 1
    if cnt == 3:
        exit(print(i + 1, j + 1))
    cnt = 0
    for dx, dy in [(0, -1), (-1, -1), (-1, 0)]:
        ni = i + dx
        nj = j + dy
        if 0 <= ni < H and 0 <= nj < W:
            if S[ni][nj] == "#":
                cnt += 1
    if cnt == 3:
        exit(print(i + 1, j + 1))
    cnt = 0
    for dx, dy in [(-1, 0), (-1, 1), (0, 1)]:
        ni = i + dx
        nj = j + dy
        if 0 <= ni < H and 0 <= nj < W:
            if S[ni][nj] == "#":
                cnt += 1
    if cnt == 3:
        exit(print(i + 1, j + 1))
    cnt = 0
    for dx, dy in [(1, 1), (1, 0), (0, 1)]:
        ni = i + dx
        nj = j + dy
        if 0 <= ni < H and 0 <= nj < W:
            if S[ni][nj] == "#":
                cnt += 1
    if cnt == 3:
        exit(print(i + 1, j + 1))


for i in range(H):
    for j in range(W):
        solve(i, j)
