n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

dp=[[-1]*(m+1) for _ in range(n)]
dp[0][0]=0
for i in range(n-1):
    for j in range(m):
        if dp[i][j]==-1:
            continue
        dp[i+1][j]=max(dp[i+1][j],dp[i][j])
        
        if 0<=j+a[i]<m+1:
            dp[i+1][j+a[i]]=max(dp[i+1][j+a[i]],dp[i][j]+b[i])

print(*dp,sep="\n")