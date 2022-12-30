H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

ans = []
for j in range(W):
    tmp = 0
    for i in range(H):
        if grid[i][j] == '#':
            tmp += 1
    ans.append(tmp)
print(*ans)
