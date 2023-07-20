from string import ascii_lowercase
from collections import deque
H, W = map(int, input().split())
S = [input() for _ in range(H)]
sx, sy = -1, -1
gx, gy = -1, -1
Edge = [[] for _ in range(26)]
alphabets = set(list(ascii_lowercase))
for i in range(H):
    for j in range(W):
        if S[i][j] == 'S':
            sx, sy = i, j
        elif S[i][j] == 'G':
            gx, gy = i, j
        elif S[i][j] in ['.', '#']:
            pass
        else:
            idx = ord(S[i][j])-97
            Edge[idx].append((i, j))
q = deque([(sx, sy)])
dp = [[-1]*W for _ in range(H)]
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dp[sx][sy] = 0
used = [False]*26
while q:
    vx, vy = q.popleft()

    if S[vx][vy] in alphabets:
        idx = ord(S[vx][vy])-97
        for ex, ey in Edge[idx]:
            if dp[ex][ey] != -1:
                continue
            dp[ex][ey] = dp[vx][vy]+1
            q.append((ex, ey))
        Edge[idx].clear()
    for dx, dy in dxy:
        nx = vx+dx
        ny = vy+dy
        if not(0 <= nx < H and 0 <= ny < W):
            continue
        if S[nx][ny] != '#':
            if dp[nx][ny] != -1:
                continue
            dp[nx][ny] = dp[vx][vy]+1
            q.append((nx, ny))

ans = dp[gx][gy]
print(ans)
