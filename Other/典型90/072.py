h, w = map(int, input().split())
import sys 
sys.setrecursionlimit(10**7)
grid = []
for _ in range(h):
    grid.append(list(input()))
ans = [-1]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False]*w for _ in range(h)]

def rec(x, y, sx, sy, n):
    if x == sx and y == sy and n>=3:
        ans[0] = max(ans[0], n)
        return

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < h and 0 <= ny < w:
            if grid[nx][ny] == '.' and visited[nx][ny] == False:
                visited[nx][ny] = True
                rec(nx, ny, sx, sy, n+1)
                visited[nx][ny] = False

for i in range(h):
    for j in range(w):
        if grid[i][j] == '.':
            rec(i, j, i, j, 0)

print(ans[0])