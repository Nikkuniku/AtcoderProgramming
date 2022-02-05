n,S=map(int,input().split())
a=list(map(int,input().split()))

dp=[[False]*(S+1) for _ in range(n+1)]
dp[0][0]=True
for i in range(n):
    for s in range(S+1):
        dp[i+1][s]|=dp[i][s]
        if s-a[i]>=0:
            dp[i+1][s]|=dp[i][s-a[i]]

ans=dp[n][S]

if ans:
    print('Yes')
else:
    print('No')