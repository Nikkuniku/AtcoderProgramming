from collections import deque
N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
collision = set()
ices = set()
q = deque([(1, 1)])
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
res = [[0]*M for _ in range(N)]
while q:
    vx, vy = q.popleft()
    res[vx][vy] += 1
    for dx, dy in dxy:
        nx = vx+dx
        ny = vy+dy
        while S[nx][ny] == '.':
            res[nx][ny] += 1
            nx += dx
            ny += dy
        if res[nx-dx][ny-dy] >= 2:
            continue
        q.append((nx-dx, ny-dy))
ans = 0
for i in range(N):
    for j in range(M):
        if res[i][j] >= 1:
            ans += 1
print(ans)
