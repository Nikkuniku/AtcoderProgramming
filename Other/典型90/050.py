n,l=map(int,input().split())
mod=10**9 + 7 

dp=[0]*(n+1)
dp[0]=1
for i in range(n):
    if i+1-l>=0:
        dp[i+1] = dp[i]+dp[i+1-l]
    else:
        dp[i+1] = dp[i]

print(dp[n]%mod)