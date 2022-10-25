n,W=map(int,input().split())
g=[]
for _ in range(n):
    g.append(list(map(int,input().split())))

dp=[[0]*(W+1) for _ in range(n+1)]

for i in range(n):
    for w in range(W+1):
        dp[i+1][w]=max(dp[i+1][w],dp[i][w])
        
        if w-g[i][0]>=0:
            dp[i+1][w]=max(dp[i+1][w],dp[i][w-g[i][0]]+g[i][1])

print(dp[n][W])