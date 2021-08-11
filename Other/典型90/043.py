from collections import deque
h, w = map(int, input().split())
rs, cs = map(int, input().split())
rt, ct = map(int, input().split())
rs, cs = rs-1, cs-1
rt, ct = rt-1, ct-1
INF = 10**8 + 9

grid = []
for _ in range(h):
    g = list(input())
    grid.append(g)

cost = [[INF]*w for _ in range(h)]
cost[rs][cs] = 0

q = deque()
for i in range(4):
    q.append((rs,cs,i,0))
dxy = [(0, -1, 0), (-1, 0, 1), (0, 1, 2), (1, 0, 3)]

while q:
    rv, cv, dict,c = q.popleft()

    for i in range(4):
        dx, dy, dir = dxy[i]
        nx = rv+dx
        ny = cv+dy
        if 0 <= nx < h and 0 <= ny < w:
            if grid[nx][ny] == '#':
                continue
            if cost[nx][ny] >= c+1 and dir != dict:
                cost[nx][ny] = c+1
                q.append((nx, ny, dir,c+1))
            elif cost[nx][ny] >= c and dir == dict:
                cost[nx][ny] = c
                q.appendleft((nx, ny, dir,c))

print(cost[rt][ct])
