n=int(input())
X,Y=map(int,input().split())
bento=[]
for _ in range(n):
    a,b=map(int,input().split())
    bento.append((a,b))
limit=301
INF=10**8
dp=[[[INF]*(limit) for _ in range(limit)] for _ in range(n+1)]
dp[0][0][0]=0
for i in range(n):
    a,b=bento[i]
    for x in range(limit):
        for y in range(limit):
            if x-a>=0 and y-b>=0:
                dp[i+1][x][y]=min(dp[i][x][y],dp[i][x-a][y-b]+1)
            else:
                dp[i+1][x][y]=dp[i][x][y]
    
    for x in range(limit-1,-1,-1):
        for y in range(limit-1,-1,-1):
            if y+1<limit:
                dp[i+1][x][y]=min(dp[i+1][x][y],dp[i+1][x][y+1])
            if x+1<limit:
                dp[i+1][x][y]=min(dp[i+1][x][y],dp[i+1][x+1][y])
ans=INF
for x in range(X,limit):
    for y in range(Y,limit):
        if ans>dp[n][x][y]:
            ans=dp[n][x][y]
if ans==INF:
    ans=-1
print(ans)