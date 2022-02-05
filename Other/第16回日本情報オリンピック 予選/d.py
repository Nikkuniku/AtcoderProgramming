n,m=map(int,input().split())
good=[int(input()) for _ in range(n)]
INF=10**18
dp=[[[INF]*m for _ in range(1<<m)] for _ in range(n+1)]
dp[0]=[[0]*m for _ in range(1<<m)]

def sgn(p,q):
    ans=1
    if p==q:
        ans=0
    return ans

for i in range(n):
    x=good[i]-1

    for s in range(1<<m):
        if (s>>x)&1:
            for v in range(m):
                for u in range(m):
                    dp[i+1][s][v] = min(dp[i+1][s][v],dp[i][s][u]+2*sgn(u,v))
        
        else:
            dp[i+1][s|(1<<x)][x]=min(dp[i][s])

print(dp[n][(1<<m)-1])