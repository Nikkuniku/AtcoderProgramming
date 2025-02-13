from sys import setrecursionlimit

setrecursionlimit(10 * 8)
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
K = 0
for i in range(H):
    for j in range(W):
        K += S[i][j] == "#"

seen = [[False] * W for _ in range(H)]


def dfs(i, j, ans=[]):
    seen[i][j] = True
    ans.append((i + 1, j + 1))
    if len(ans) == K:
        print(K)
        for c in ans:
            print(*c)
        exit(0)
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in dxy:
        ni = i + dx
        nj = j + dy
        if not (0 <= ni < H and 0 <= nj < W):
            continue
        if seen[ni][nj]:
            continue
        if S[ni][nj] == ".":
            continue
        dfs(ni, nj, ans)
    ans.pop()
    seen[i][j] = False


for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            dfs(i, j, [])
