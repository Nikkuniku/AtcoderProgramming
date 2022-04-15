from collections import deque
island = []
for _ in range(10):
    island.append(list(input()))
points = []
cnt = 0
for i in range(10):
    for j in range(10):
        if island[i][j] == 'o':
            points.append((i, j))
            cnt += 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def solve():
    re = False
    q = deque([points[0]])
    dist = [[-1]*10 for _ in range(10)]
    dist[points[0][0]][points[0][1]] = 0
    while q:
        vx, vy = q.popleft()

        for k in range(4):
            nx = vx+dx[k]
            ny = vy+dy[k]
            if 0 <= nx < 10 and 0 <= ny < 10:
                if island[nx][ny] == 'x':
                    continue
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[vx][vy]+1
                    q.append((nx, ny))

    tmp = 0
    for i in range(10):
        for j in range(10):
            if dist[i][j] >= 0:
                tmp += 1
    if tmp == cnt+1:
        re = True

    return re


for i in range(10):
    for j in range(10):
        if island[i][j] == 'x':
            island[i][j] = 'o'
            Flg = solve()
            if Flg:
                print('YES')
                exit(0)
            island[i][j] = 'x'
print('NO')
