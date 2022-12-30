n=int(input())
a=list(map(int,input().split()))
p=998244353
dp=[[0]*10 for _ in range(n+1)]

for j in range(10):
    if j==a[0]:
        dp[0][j]=1

for i in range(n-1):
    for j in range(10):
        dp[i+1][(j+a[i+1])%10]+=dp[i][j]
        dp[i+1][(j*a[i+1])%10]+=dp[i][j]
        dp[i+1][(j+a[i+1])%10]%=p
        dp[i+1][(j*a[i+1])%10]%=p

print(*dp[n-1],sep="\n")