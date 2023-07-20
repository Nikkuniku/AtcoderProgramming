T = int(input())
G = [list(map(int, input().split())) for _ in range(T)]
dp = [0]*(T+2)
for t in range(T+2):
    for i in range(t):
        for j in range(i+1, t):
            dp[t] = max(dp[t], dp[i]+G[i][j-1])
print(dp[T+1])
