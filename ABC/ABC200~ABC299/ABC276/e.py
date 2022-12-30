from collections import defaultdict, deque
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]
edge = []
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
s = -1
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            s = W*i+j
        if grid[i][j] == '#':
            continue
        for dx, dy in dxy:
            if 0 <= i+dx < H and 0 <= j+dy < W:
                if grid[i+dx][j+dy] == '.' or grid[i+dx][j+dy] == 'S':
                    edge.append((W*i+j, W*(i+dx)+j+dy))
print(edge)
