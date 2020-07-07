n=int(input())
a=list(map(int,input().split()))

dp=[10**9]*n
dp[0]=0

for i in range(1,n):
    if i==1:
        dp[i]=dp[0]+abs(a[i]-a[i-1])
    else:
        dp[i]=min(dp[i-1]+abs(a[i]-a[i-1]),dp[i-2]+abs(a[i]-a[i-2]))

print(dp[-1])