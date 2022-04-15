n,x=map(int,input().split())

dp=[[False]*(x+3) for _ in range(n+1)]
dp[0][0]=True

for i in range(n):
    a,b=map(int,input().split())

    for j in range(x+1):
        if j>=a:
            dp[i+1][j]|=dp[i][j-a]
        if j>=b:
            dp[i+1][j]|=dp[i][j-b]

ans='No'
if dp[n][x]:
    ans='Yes'
print(ans)