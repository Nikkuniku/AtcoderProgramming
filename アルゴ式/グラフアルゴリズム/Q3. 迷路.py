from collections import deque
H, W = map(int, input().split())
sx, sy, gx, gy = map(int, input().split())
Maze = [input() for _ in range(H)]
q = deque([(sx, sy)])
dist = [[-1]*W for _ in range(H)]
dist[sx][sy] = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while q:
    vx, vy = q.popleft()

    for k in range(4):
        nx, ny = vx+dx[k], vy+dy[k]
        if 0 <= nx < H and 0 <= ny < W:
            if dist[nx][ny] != -1:
                continue
            if Maze[nx][ny] == 'B':
                continue
            dist[nx][ny] = dist[vx][vy]+1
            q.append((nx, ny))

print(dist[gx][gy])
