n=int(input())
a=list(map(int,input().split()))

inf=10**19

cum=[0]
for i in range(n):
    cum.append(cum[-1]+a[i])

dp=[[0]*(n+1) for _ in range(n+1)]

for i in range(n+1,-1,-1):
    for j in range(n+1):
        if j-i>=2:
            tmp=inf
            for k in range(i+1,j):
                tmp=min(tmp,dp[i][k]+dp[k][j])

            dp[i][j]=cum[j]-cum[i]+tmp
    
print(dp[0][n])
