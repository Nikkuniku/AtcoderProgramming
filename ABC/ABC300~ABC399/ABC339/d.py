from collections import deque

N = int(input())
S = [list(input()) for _ in range(N)]
px, py = -1, -1
qx, qy = -1, -1
blocked = set()
for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            blocked.add(100 * i + j)
        if S[i][j] == "P":
            if (px, py) == (-1, -1):
                px = i
                py = j
            else:
                qx = i
                qy = j
dist = [-1] * 59595960
s = px * 1000000 + py * 10000 + qx * 100 + qy
dist[s] = 0
q = deque([s])
dxy = [(0, -1), (0, 1), (-1, 0), (1, 0)]
seen = set()
seen.add(s)
while q:
    t = q.popleft()
    vx = t // 1000000
    vy = (t // 10000) % 100
    wx = (t // 100) % 100
    wy = t % 100
    val = dist[t]
    for dx, dy in dxy:
        # プレイヤー1
        ax = vx + dx
        ay = vy + dy
        # プレイヤー2
        bx = wx + dx
        by = wy + dy
        if 100 * ax + ay in blocked:
            ax = vx
            ay = vy
        if 100 * bx + by in blocked:
            bx = wx
            by = wy
        if not (0 <= ax < N and 0 <= ay < N):
            ax = vx
            ay = vy
        if not (0 <= bx < N and 0 <= by < N):
            bx = wx
            by = wy
        next = ax * 1000000 + ay * 10000 + bx * 100 + by
        if next in seen:
            continue
        seen.add(next)
        dist[next] = val + 1
        if 100 * ax + ay == 100 * bx + by:
            exit(print(val + 1))
        q.append(next)
ans = -1
kouho = []
for i in range(N):
    for j in range(N):
        s = i * 1000000 + j * 10000 + i * 100 + j
        if s in seen and dist[s] > 0:
            kouho.append(dist[s])
if kouho:
    ans = min(kouho)
print(ans)
