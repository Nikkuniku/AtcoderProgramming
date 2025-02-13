from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
visited = [[False] * W for _ in range(H)]
conn = [[-1] * W for _ in range(H)]
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
q = deque()
M = 0
R = 0
for i in range(H):
    for j in range(W):
        if visited[i][j]:
            continue
        if S[i][j] == ".":
            R += 1
            continue
        q.append((i, j))
        visited[i][j] = True
        conn[i][j] = M
        while q:
            vi, vj = q.popleft()
            for dx, dy in dxy:
                ni = vi + dx
                nj = vj + dy
                if not (0 <= ni < H and 0 <= nj < W):
                    continue
                if visited[ni][nj]:
                    continue
                if S[ni][nj] == "#":
                    conn[ni][nj] = M
                    visited[ni][nj] = True
                    q.append((ni, nj))
        M += 1
ans = 0
MOD = 998244353
movinv = pow(R, -1, MOD)
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            continue
        roots = set()
        for dx, dy in dxy:
            ni = i + dx
            nj = j + dy
            if not (0 <= ni < H and 0 <= nj < W):
                continue
            if S[ni][nj] == "#":
                roots.add(conn[ni][nj])
        ans += M - (len(roots) - 1)
ans *= movinv
ans %= MOD
print(ans)
