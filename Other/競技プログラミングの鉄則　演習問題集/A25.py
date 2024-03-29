h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]
dp = [[0]*w for _ in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if j+1 < w and grid[i][j+1] == '.':
            dp[i][j+1] += dp[i][j]
        if i+1 < h and grid[i+1][j] == '.':
            dp[i+1][j] += dp[i][j]

print(dp[h-1][w-1])
