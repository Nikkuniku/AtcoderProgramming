from collections import deque
from heapq import heapify, heappop, heappush

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
N = int(input())
Med = []
INF = 1 << 60
Set_Meds = set()
for i in range(N):
    r, c, e = map(int, input().split())
    r -= 1
    c -= 1
    Med.append((r, c, e))
    Set_Meds.add((r, c))
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
Points = [(sx, sy)]
for r, c, _ in Med:
    Points.append((r, c))
Points.append((gx, gy))


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
    s, t = Points[i]
    dist = BFS(s, t)
    for j in range(N + 2):
        x, y = Points[j]
        cost[i][j] = dist[x][y]
HitPoint = [-1] * (N + 2)
HitPoint[0] = 0
q = [(0, 0)]
heapify(q)
seen = [False] * (N + 2)
while q:
    v, i = heappop(q)
    seen[i] = True
    # 薬のあるところ
    for j in range(1, N + 1):
        c = cost[i][j]
        if c == INF:
            continue
        _, _, e = Med[j - 1]
        if not seen[j] and v - c > HitPoint[j]:
            HitPoint[j] = max(v - c, e)
            heappush(q, (HitPoint[j], j))
    # ゴールのあるところ
    c = cost[i][N + 1]
    if c == INF:
        continue
    if not seen[N + 1] and v - c > HitPoint[N + 1]:
        HitPoint[N + 1] = v - c
        break
ans = "No"
if HitPoint[N + 1] >= 0:
    ans = "Yes"
print(*cost, sep="\n")
print(ans)
