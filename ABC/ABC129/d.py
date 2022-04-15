from collections import defaultdict
H, W = map(int, input().split())
grid = []
ans = [[0]*W for _ in range(H)]
ans_2 = [[0]*W for _ in range(H)]
points = defaultdict(int)
for i in range(H):
    grid.append(list(input()))

for i in range(H):
    pre = -1
    for j in range(W):
        if grid[i][j] == '#':
            if j == 0:
                pre = j
                continue
            ans[i][j-1] = j-pre-1
            pre = j
    ans[i][W-1] = W-pre-1

for j in range(W):
    pre = -1
    for i in range(H):
        if grid[i][j] == '#':
            if i == 0:
                pre = i
                continue
            ans_2[i-1][j] = i-pre-1
            pre = i
    ans_2[H-1][j] = H-pre-1
for i in range(H):
    for j in range(W-2, -1, -1):
        if grid[i][j] == '#':
            continue
        ans[i][j] += ans[i][j+1]

for j in range(W):
    for i in range(H-2, -1, -1):
        if grid[i][j] == '#':
            continue
        ans_2[i][j] += ans_2[i+1][j]
re = 0
for i in range(H):
    for j in range(W):
        re = max(re, ans[i][j]+ans_2[i][j]-1)

print(re)
