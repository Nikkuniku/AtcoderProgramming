h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(list(map(int, input().split())))
ans = 0
operation = []
for i in range(h):
    for j in range(w):
        if grid[i][j] % 2 == 0:
            continue
        if j+1 < w:
            grid[i][j] -= 1
            grid[i][j+1] += 1
            operation.append([i+1, j+1, i+1, j+1+1])
            ans += 1
        else:
            if i+1 < h:
                grid[i][j] -= 1
                grid[i+1][j] += 1
                operation.append([i+1, j+1, i+1+1, j+1])
                ans += 1

print(ans)
for i in range(ans):
    print(*operation[i])
