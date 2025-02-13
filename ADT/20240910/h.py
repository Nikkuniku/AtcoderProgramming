from collections import deque

N = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
S = [list(input()) for _ in range(N)]
ax -= 1
ay -= 1
bx -= 1
by -= 1
INF = 1 << 60
dist = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
q = deque()
for k in range(4):
    q.append((ax, ay, k))
    dist[ax][ay][k] = 1
dxy = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
while q:
    vx, vy, dir = q.popleft()
    for k in range(4):
        dx, dy = dxy[k]
        nx = vx + dx
        ny = vy + dy
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if S[nx][ny] == "#":
            continue
        if dist[nx][ny][k] > dist[vx][vy][dir] + (1 if k != dir else 0):
            dist[nx][ny][k] = dist[vx][vy][dir] + (1 if k != dir else 0)
            if k == dir:
                q.appendleft((nx, ny, k))
            else:
                q.append((nx, ny, k))
ans = min(dist[bx][by])
if ans == INF:
    ans = -1
print(ans)
