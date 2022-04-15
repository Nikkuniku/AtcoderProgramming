n=int(input())
t=list(map(int,input().split()))
T=sum(t)
V=sum(t)+3
dp=[[False]*V for _ in range(n+1)]
dp[0][0]=True
for i in range(n):
    for j in range(V):
        dp[i+1][j]|=dp[i][j]
        if j-t[i]>=0:
            dp[i+1][j]|=dp[i][j-t[i]]

ans=10**9
for k in range(V):
    if dp[n][k]:
        p=max(k,T-k)
        if ans>p:
            ans=p

print(ans)