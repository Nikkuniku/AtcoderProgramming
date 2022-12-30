n,m=map(int,input().split())
INF = float('inf')
cost=[[INF]*n for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())

    cost[a-1][b-1]=c

ans=0
for k in range(n):
    tmp=0
    for i in range(n):
        for j in range(n):
            if cost[i][k]!=INF and cost[k][j]!=INF:
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
                if i!=j:
                    tmp+=cost[i][j]
                    continue
            if cost[i][j]!=INF:
                if i!=j:
                    tmp+=cost[i][j]
                    continue
    ans+=tmp

print(ans)