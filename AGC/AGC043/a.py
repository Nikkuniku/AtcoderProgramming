from collections import deque
h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(input())

q = deque()
INF = 1000
ans = [[INF]*w for _ in range(h)]
dx = [0, 1]
dy = [1, 0]
isBlack = False
if grid[0][0] == '.':
    ans[0][0] = 0
else:
    ans[0][0] = 1
    isBrack = True
q.append((0, 0))
while q:
    vx, vy = q.popleft()
    if grid[vx][vy] == '#':
        isBlack = True
    else:
        isBlack = False

    for k in range(2):
        nx = vx+dx[k]
        ny = vy+dy[k]
        if 0 <= nx < h and 0 <= ny < w:
            if ans[nx][ny] > ans[vx][vy]:
                if grid[nx][ny] == '.':
                    ans[nx][ny] = ans[vx][vy]
                else:
                    if isBlack:
                        ans[nx][ny] = ans[vx][vy]
                    else:
                        ans[nx][ny] = ans[vx][vy]+1
                q.append((nx, ny))
print(ans[h-1][w-1])
