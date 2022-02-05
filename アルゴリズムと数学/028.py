n=int(input())
h=list(map(int,input().split()))

dp=[0]*n

for i in range(n-1):
    dp[i+1]=dp[i]+abs(h[i+1]-h[i])
    if i-1>=0:
        dp[i+1]=min(dp[i+1],dp[i-1]+abs(h[i+1]-h[i-1]))

print(dp[n-1])