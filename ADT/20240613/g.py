from collections import deque

N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
dist = [[0] * M for _ in range(N)]
q = deque([(1, 1, -1)])
dist[1][1] = 1
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
stopped = set()
while q:
    vx, vy, dir = q.popleft()
    if dir == -1:
        for k in range(4):
            dx, dy = dxy[k]
            nx = vx + dx
            ny = vy + dy
            if S[nx][ny] == "#":
                continue
            dist[nx][ny] = 1
            q.append((nx, ny, k))
    else:
        dx, dy = dxy[dir]
        nx = vx + dx
        ny = vy + dy
        if S[nx][ny] == "#":
            if (vx, vy) in stopped:
                continue
            q.append((vx, vy, -1))
            stopped.add((vx, vy))
        else:
            dist[nx][ny] = 1
            q.append((nx, ny, dir))
ans = 0
for i in range(N):
    for j in range(M):
        ans += dist[i][j]
print(ans)
