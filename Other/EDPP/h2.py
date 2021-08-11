h, w = map(int, input().split())
grid = []
for _ in range(h):
    grid.append(list(input()))

dp = [[0]*(w+1) for _ in range(h+1)]
dp[1][1] = 1
mod = 10**9 + 7
for i in range(h):
    for j in range(w):
        if grid[i][j] == '.':
            dp[i+1][j+1] += dp[i+1][j]+dp[i][j+1]
            dp[i+1][j+1] %= mod
print(dp[h][w])
