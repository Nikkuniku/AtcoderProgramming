n = int(input())
grid = [[0]*n for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(i+1):
        grid[i][j] = a[j]

ans = [[0]*n for _ in range(n)]
ans[0][0] = grid[0][0]
for i in range(n):
    for j in range(n):
        if i-1 >= 0:
            ans[i][j] = max(ans[i][j], ans[i-1][j]+grid[i][j])
            if j-1 >= 0:
                ans[i][j] = max(ans[i][j], ans[i-1][j-1]+grid[i][j])

print(max(ans[n-1]))
