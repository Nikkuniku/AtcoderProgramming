from sys import setrecursionlimit

setrecursionlimit(10**8)
H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]
seen = [[False] * W for _ in range(H)]
ans = 0
dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def dfs(vx, vy, px=-1, py=-1, c=0):
    global ans
    if c == K:
        ans += 1
        return
    seen[vx][vy] = True
    for dx, dy in dxy:
        nx = vx + dx
        ny = vy + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if S[nx][ny] == "#":
            continue
        if seen[nx][ny]:
            continue
        if nx == px and ny == py:
            continue
        seen[nx][ny] = True
        dfs(nx, ny, vx, vy, c + 1)
        seen[nx][ny] = False
    seen[vx][vy] = False


for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            dfs(i, j)
print(ans)
