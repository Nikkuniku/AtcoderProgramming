from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
sx, sy = -1, -1
gx, gy = -1, -1
for i in range(H):
    for j in range(W):
        if S[i][j] == "s":
            sx, sy = i, j
        elif S[i][j] == "g":
            gx, gy = i, j
q = deque([(sx, sy)])
dist = [[-1] * W for _ in range(H)]
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dist[sx][sy] = 0
while q:
    vx, vy = q.popleft()
    for dx, dy in dxy:
        nx = vx + dx
        ny = vy + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if dist[nx][ny] != -1:
            continue
        if S[nx][ny] == "#":
            dist[nx][ny] = dist[vx][vy] + 1
            q.append((nx, ny))
        else:
            dist[nx][ny] = dist[vx][vy]
            q.appendleft((nx, ny))
ans = "YES" if dist[gx][gy] <= 2 else "NO"
print(ans)
