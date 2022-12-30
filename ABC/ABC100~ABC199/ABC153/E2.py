h,n=map(int,input().split())
a,b=[],[]

for _ in range(n):
    a_i,b_i = map(int,input().split())
    a.append(a_i)
    b.append(b_i)

INF = float('inf')

dp=[[INF]*(h+1) for _ in range(n+1)]
dp[0][0]=0

for i in range(n+1):
    for w in range(h+1):
        if i>0:
            

            if w-a[i-1]>=0:
                dp[i][w]=min(dp[i-1][w-a[i-1]]+b[i-1],dp[i-1][w])
                dp[i][w]=min(dp[i-1][w],dp[i][w-a[i-1]]+b[i-1])
            
            dp[i][w]=min(dp[i][w],dp[i-1][w])

print(*dp,sep="\n")