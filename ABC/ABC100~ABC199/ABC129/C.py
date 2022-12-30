n,m=map(int,input().split())
a = []

mod = 1000000007

dp=[0]*(n+1)

dp[0]=1
dp[1]=1
d={}
for j in range(n+1):
    d[j]=0

for _ in range(m):
    s = int(input())
    d[s]=1
    dp[s]=0

for i in range(2,n+1):
    if d[i]==1:
        dp[i] = 0
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[-1]%mod) 
