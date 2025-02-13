from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
dxy = [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]
q = deque()
gx, gy = -1, -1
for i in range(H):
    for j in range(W):
        if S[i][j] == "S":
            q.append((i, j, 0))
            q.append((i, j, 1))
        if S[i][j] == "G":
            gx = i
            gy = j
dist = [[[-1] * W for _ in range(H)] for _ in range(2)]
for x, y, d in q:
    dist[d][x][y] = 0
while q:
    vx, vy, dir = q.popleft()
    for dx, dy in dxy[dir ^ 1]:
        nx = vx + dx
        ny = vy + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if S[nx][ny] == "#":
            continue
        if dist[dir ^ 1][nx][ny] != -1:
            continue
        dist[dir ^ 1][nx][ny] = dist[dir][vx][vy] + 1
        q.append((nx, ny, dir ^ 1))
ans = 1 << 60
if dist[0][gx][gy] != -1:
    ans = min(ans, dist[0][gx][gy])
if dist[1][gx][gy] != -1:
    ans = min(ans, dist[1][gx][gy])
if ans == 1 << 60:
    ans = -1
print(ans)
