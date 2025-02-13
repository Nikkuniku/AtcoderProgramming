from collections import deque

N = int(input())
ax, ay = map(int, input().split())
ax -= 1
ay -= 1
bx, by = map(int, input().split())
bx -= 1
by -= 1
S = [list(input()) for _ in range(N)]
q = deque()
dxy = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
INF = 1 << 60
dist = [[[INF] * N for _ in range(N)] for _ in range(4)]
for k in range(4):
    dist[k][ax][ay] = 0
    dx, dy = dxy[k]
    nx, ny = ax + dx, ay + dy
    if not (0 <= nx < N and 0 <= ny < N):
        continue
    if S[nx][ny] == "#":
        continue
    dist[k][nx][ny] = 1
    q.append((nx, ny, k))
while q:
    vx, vy, direction = q.popleft()
    for k in range(4):
        dx, dy = dxy[k]
        nx, ny = vx + dx, vy + dy
        cd = dist[direction][vx][vy]
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if S[nx][ny] == "#":
            continue
        nd = cd + (k != direction)
        if dist[k][nx][ny] > nd:
            dist[k][nx][ny] = nd
            if k != direction:
                q.append((nx, ny, k))
            else:
                q.appendleft((nx, ny, k))
ans = 1 << 60
isOK = False
for k in range(4):
    if dist[k][bx][by] != INF:
        ans = min(ans, dist[k][bx][by])
        isOK = True
if not isOK:
    ans = -1
print(ans)
