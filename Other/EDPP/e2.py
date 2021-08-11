n,W=map(int,input().split())
good=[]
V=0
for _ in range(n):
    w,v=map(int,input().split())
    V+=v
    good.append([w,v])
INF=10**9
dp=[[INF]*(V+1) for _ in range(n+1)]
dp[0][0]=0

for i in range(n):
    for v in range(V+1):
        dp[i+1][v]=min(dp[i+1][v],dp[i][v])
        g=good[i]
        if v-g[1]>=0:
            dp[i+1][v]=min(dp[i+1][v],dp[i][v-g[1]]+g[0])

ans=0
for v in range(V+1):
    if dp[n][v]<=W:
        ans=max(ans,v)

print(ans)