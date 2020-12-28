n=int(input())
a=list(map(int,input().split()))
A=int(input())

dp=[[0]*(A+1) for _ in range(n+1)]
dp[0][0]=1

for i in range(n+1):
    for w in range(A+1):
        if i>0:
            if w-a[i-1]>=0:
                dp[i][w]=dp[i-1][w-a[i-1]]+dp[i-1][w]
            else:
                dp[i][w]=dp[i-1][w]

ans=dp[n][A]

print(ans)