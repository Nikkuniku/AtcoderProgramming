from collections import deque

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
q = deque()
dist = [[[-1] * 4 for _ in range(M)] for _ in range(N)]
for d in range(4):
    dist[1][1][d] = 0
    q.append((1, 1, d))
blocked = set()
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    vx, vy, dir = q.popleft()
    if dir != -1:
        dx, dy = dxy[dir]
        nx = vx + dx
        ny = vy + dy
        if dist[nx][ny][dir] != -1:
            continue
        if S[nx][ny] == ".":
            dist[nx][ny][dir] = dist[vx][vy][dir] + 1
            q.append((nx, ny, dir))
        else:
            q.append((vx, vy, -1))
    else:
        for d in range(4):
            dx, dy = dxy[d]
            nx = vx + dx
            ny = vy + dy
            if S[nx][ny] == "#":
                continue
            if dist[nx][ny][d] != -1:
                continue
            dist[nx][ny][d] = dist[vx][vy][d] + 1
            q.append((nx, ny, d))
ans = 0
for i in range(N):
    for j in range(M):
        isReached = False
        for d in range(4):
            isReached |= dist[i][j][d] != -1
        ans += isReached
print(ans)
