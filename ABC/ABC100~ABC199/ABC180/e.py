n=int(input())
node=[tuple(map(int,input().split())) for _ in range(n)]
INF = 10**18

dp=[[INF]*n for _ in range(1<<n)]
dp[0][0]=0

for s in range(1<<n):
    for v in range(n):
        if (s>>v)&1:
            continue
        a,b,c=node[v]
        for u in range(n):
            p,q,r=node[u]
            if dp[s][u]+abs(p-a)+abs(q-b)+max(0,r-c)<dp[s|(1<<v)][v]:
                dp[s|(1<<v)][v]=dp[s][u]+abs(p-a)+abs(q-b)+max(0,r-c)

ans=dp[(1<<n)-1][0]
print(ans)