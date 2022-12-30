from collections import deque
N, M = map(int, input().split())
Grid = [input() for _ in range(N)]
INF = 1 << 30


def BFS(distarray, s):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    q = deque()
    for i in range(N):
        for j in range(M):
            if distarray[i][j] != -1:
                q.append((i, j))
    while q:
        vx, vy = q.popleft()

        for k in range(4):
            ex = vx+dx[k]
            ey = vy+dy[k]
            if 0 <= ex < N and 0 <= ey < M:
                if distarray[ex][ey] > distarray[vx][vy]+1:
                    distarray[ex][ey] = distarray[vx][vy]+1
                    q.append((ex, ey))
    dist2 = [[INF]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if Grid[i][j] == s:
                dist2[i][j] = distarray[i][j]

    return dist2


dist = [[INF]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if Grid[i][j] == 'S':
            dist[i][j] = 0

for s in list('123456789G'):
    dist = BFS(dist, s)
ans = []
for i in range(N):
    for j in range(M):
        if dist[i][j] != INF:
            ans.append(dist[i][j])
print(min(ans) if ans else -1)
