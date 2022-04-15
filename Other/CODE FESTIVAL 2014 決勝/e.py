n=int(input())
r=list(map(int,input().split()))

dp=[[0]*n for _ in range(2)]
dp[0][-1]=1
dp[1][-1]=1

for i in range(n-2,-1,-1):
    p=r[i]
    for j in range(i+1,n):
        q=r[j]
        if p>q:
            dp[1][i]=max(dp[1][i],dp[0][j]+1)
            dp[0][i]=max(dp[0][i],1)
        elif p<q:
            dp[0][i]=max(dp[0][i],dp[1][j]+1)
            dp[1][i]=max(dp[1][i],1)
ans=max(dp[0][0],dp[1][0])
if ans<3:
    ans=0
print(ans)          