V,E=map(int,input().split())
INF=10**9
cost=[[INF]*V for _ in range(V)] 
for _ in range(E):
    s,t,d=map(int,input().split())
    cost[s][t]=d

dp=[[INF]*V for _ in range(1<<V)]
dp[0][0]=0
for s in range(1<<V):
    for v in range(V):
        # まだvのノードを通っていない
        if (s>>v)&1:
            continue
        for u in range(V):
            if dp[s][u]+cost[u][v]<dp[s|(1<<v)][v]:
                dp[s|(1<<v)][v] = dp[s][u]+cost[u][v]

ans=dp[(1<<V)-1][0]
if ans==INF:
    ans=-1
print(ans)