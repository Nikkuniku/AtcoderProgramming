n=int(input())
t=list(map(int,input().split()))

t=sorted(t,reverse=True)
s=sum(t)
dp=[[False]*(s+1) for _ in range(n+1)]
dp[0][0]=True

for i in range(n):
    for j in range(s):
        if j>=t[i]:
            dp[i+1][j] = dp[i][j-t[i]] or dp[i][j]
        else:
            dp[i+1][j] = dp[i][j]

ans=0
for k in range(s//2 + 1):
    if dp[n][k]:
        ans=max(ans,k)

print(s-ans)