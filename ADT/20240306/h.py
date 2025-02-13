N = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())
ax -= 1
ay -= 1
bx -= 1
by -= 1
S = [list(input()) for _ in range(N)]
dist = [[-1] * N for _ in range(N)]
from heapq import heapify, heappop, heappush
from collections import deque

dist[ax][ay] = 0
q = [(0, ax, ay)]
heapify(q)
while q:
    _, vx, vy = heappop(q)
    dxy = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    for dx, dy in dxy:
        nx = vx + dx
        ny = vy + dy
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if S[nx][ny] == "." and dist[nx][ny] == -1:
            dist[nx][ny] = dist[vx][vy] + 1
            heappush(q, (dist[nx][ny], nx, ny))
            nx += dx
            ny += dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            while S[nx][ny] == "." and dist[nx][ny] == -1:
                dist[nx][ny] = dist[vx][vy] + 1
                heappush(q, (dist[nx][ny], nx, ny))
print(dist[bx][by])
