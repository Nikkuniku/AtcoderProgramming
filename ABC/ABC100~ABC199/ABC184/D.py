a,b,c =map(int,input().split())

dp=[[[0.0]*(101) for _ in range(101)] for _ in range(101) ]
dp[99][99][99]=1.0

for k in range(99,-1,-1):
    for j in range(99,-1,-1):
        for i in range(99,-1,-1):
            if i+j+k==0:
                continue

            dp[k][i][j]=( i*dp[k][i+1][j] + j*dp[k][i][j+1] + k*dp[k+1][i][j] )/(i+j+k) + 1


print(dp[c][a][b])