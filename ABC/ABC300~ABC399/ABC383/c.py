from collections import deque

H, W, D = map(int, input().split())
S = [list(input()) for _ in range(H)]
INF = 1 << 60
dist = [[INF] * W for _ in range(H)]
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q = deque()
for i in range(H):
    for j in range(W):
        if S[i][j] == "H":
            q.append((i, j))
for a, b in q:
    dist[a][b] = 0
while q:
    vx, vy = q.popleft()
    for dx, dy in dxy:
        nx = vx + dx
        ny = vy + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if S[nx][ny] == "#":
            continue
        if dist[nx][ny] != INF:
            continue
        dist[nx][ny] = dist[vx][vy] + 1
        q.append((nx, ny))
ans = 0
for i in range(H):
    for j in range(W):
        if dist[i][j] <= D:
            ans += 1
print(ans)
