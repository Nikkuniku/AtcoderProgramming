from os import sep


h, w, n, m = map(int, input().split())
grid = [[0]*w for _ in range(h)]
for _ in range(n):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    grid[a][b] = 1
INF = -1
for _ in range(m):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    grid[c][d] = -1

for i in range(h):
    light = False
    Block = False
    for j in range(w):
        if grid[i][j] != 0 and grid[i][j] != -1:
            if grid[i][j] == 1:
                light = True
                Block = False
        elif grid[i][j] == -1:
            light = False
            Block = True
        elif grid[i][j] == 0:
            if light:
                grid[i][j] = 2
for i in range(h):
    light = False
    Block = False
    for j in range(w-1, -1, -1):
        if grid[i][j] != 0 and grid[i][j] != INF:
            if grid[i][j] == 1:
                light = True
                Block = False
        elif grid[i][j] == INF:
            light = False
            Block = True
        elif grid[i][j] == 0:
            if light:
                grid[i][j] = 2
for j in range(w):
    light = False
    Block = False
    for i in range(h):
        if grid[i][j] != 0 and grid[i][j] != INF:
            if grid[i][j] == 1:
                light = True
                Block = False
        elif grid[i][j] == INF:
            light = False
            Block = True
        elif grid[i][j] == 0:
            if light:
                grid[i][j] = 2
for j in range(w):
    light = False
    Block = False
    for i in range(h-1, -1, -1):
        if grid[i][j] != 0 and grid[i][j] != INF:
            if grid[i][j] == 1:
                light = True
                Block = False
        elif grid[i][j] == INF:
            light = False
            Block = True
        elif grid[i][j] == 0:
            if light:
                grid[i][j] = 2

ans = 0
for i in range(h):
    for j in range(w):
        if 1 <= grid[i][j] <= 2:
            ans += 1
print(ans)
