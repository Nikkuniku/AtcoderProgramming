n=int(input())
w=list(map(int,input().split()))

dp=[[0]*(n+1) for _ in range(n+1)]

for i in range(n+1,-1,-1):
    for j in range(i+2,n+1):
        
        if dp[i+1][j-1]==j-i-2:
            if abs(w[i]-w[j-1])<=1:
                dp[i][j]=max(dp[i][j],j-i)
            else:
                dp[i][j]=max(dp[i][j],j-i-2)

        for k in range(i+1,j):
            dp[i][j] = max(dp[i][j],dp[i][k]+dp[k][j])
            
print(dp[0][n])