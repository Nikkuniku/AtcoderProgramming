h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(list(input()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
s = set([1, 2, 3, 4, 5])

for i in range(h):
    for j in range(w):
        if grid[i][j] != '.':
            continue

        t = s.copy()
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if grid[nx][ny] != '.':
                    t.discard(int(grid[nx][ny]))

        grid[i][j] = min(t)

for i in range(h):
    print(*grid[i], sep="")
