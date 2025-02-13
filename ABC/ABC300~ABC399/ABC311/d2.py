from collections import deque

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
dist = [[[-1] * M for _ in range(N)] for _ in range(5)]
q = deque([(1, 1, 4)])
dist[4][1][1] = 0
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    vx, vy, dir = q.popleft()
    if dir == 4:
        for k in range(4):
            dx, dy = dxy[k]
            nx = vx + dx
            ny = vy + dy
            if S[nx][ny] == "#":
                continue
            if dist[k][nx][ny] != -1:
                continue
            dist[k][nx][ny] = dist[dir][vx][vy] + 1
            q.append((nx, ny, k))
    else:
        dx, dy = dxy[dir]
        nx = vx + dx
        ny = vy + dy
        if S[nx][ny] == "#":
            if dist[4][vx][vy] != -1:
                continue
            dist[4][vx][vy] = dist[dir][vx][vy]
            q.append((vx, vy, 4))
        else:
            if dist[dir][nx][ny] != -1:
                continue
            dist[dir][nx][ny] = dist[dir][vx][vy] + 1
            q.append((nx, ny, dir))
ans = 0
for i in range(N):
    for j in range(M):
        isOK = False
        for k in range(5):
            isOK |= dist[k][i][j] >= 0
        ans += isOK
print(ans)
