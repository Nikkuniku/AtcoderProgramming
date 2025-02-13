from collections import deque

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
N = int(input())
Med = []
INF = 1 << 60
Medset = set()
for i in range(N):
    r, c, e = map(int, input().split())
    r -= 1
    c -= 1
    Med.append((r, c, e))
    Medset.add((r, c))
cost = [[INF] * (N + 2) for _ in range(N + 2)]
sx, sy = -1, -1
gx, gy = -1, -1
for i in range(H):
    for j in range(W):
        if A[i][j] == "S":
            sx = i
            sy = j
        if A[i][j] == "T":
            gx = i
            gy = j
Points = [(sx, sy, 0)]
for r, c, e in Med:
    Points.append((r, c, e))
Points.append((gx, gy, 0))


def BFS(s, t):
    q = deque([(s, t)])
    res = [[INF] * W for _ in range(H)]
    res[s][t] = 0
    dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    while q:
        vx, vy = q.popleft()
        for dx, dy in dxy:
            nx = vx + dx
            ny = vy + dy
            if not (0 <= nx < H and 0 <= ny < W):
                continue
            if A[nx][ny] == "#":
                continue
            if res[nx][ny] != INF:
                continue
            res[nx][ny] = res[vx][vy] + 1
            q.append((nx, ny))
    return res


for i in range(N + 2):
    s, t, _ = Points[i]
    dist = BFS(s, t)
    for j in range(N + 2):
        x, y, _ = Points[j]
        cost[i][j] = dist[x][y]

Edge = [[] for _ in range(N + 2)]
for i in range(N + 2):
    for j in range(N + 2):
        if i == j:
            continue
        if cost[i][j] <= Points[i][2]:
            Edge[i].append(j)
q = deque([0])
dist = [-1] * (N + 2)
dist[0] = 0
while q:
    v = q.popleft()
    for e in Edge[v]:
        if dist[e] != -1:
            continue
        dist[e] = dist[v] + 1
        q.append(e)
ans = "Yes" if dist[-1] != -1 else "No"
print(ans)
