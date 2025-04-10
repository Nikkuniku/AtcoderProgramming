from collections import deque

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
A, B, C, D = map(int, input().split())
A -= 1
B -= 1
C -= 1
D -= 1
q = deque([(A, B)])
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dxy2 = [(-2, 0), (2, 0), (0, -2), (0, 2)]
INF = 1 << 60
dist = [[INF] * W for _ in range(H)]
dist[A][B] = 0
while q:
    vx, vy = q.popleft()
    for dx, dy in dxy:
        nx = vx + dx
        ny = vy + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if S[nx][ny] == ".":
            if dist[vx][vy] < dist[nx][ny]:
                dist[nx][ny] = dist[vx][vy]
                q.appendleft((nx, ny))
        else:
            if dist[vx][vy] + 1 < dist[nx][ny]:
                dist[nx][ny] = dist[vx][vy] + 1
                q.append((nx, ny))
    for dx, dy in dxy2:
        nx = vx + dx
        ny = vy + dy
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if dist[vx][vy] + 1 < dist[nx][ny]:
            dist[nx][ny] = dist[vx][vy] + 1
            q.append((nx, ny))
print(dist[C][D])
