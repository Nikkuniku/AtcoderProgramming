N=int(input())
dp=[]
for j in range(N+1):
    dp.append([0,0,0])

for i in range(N):
    a,b,c = map(int,input().split())
    if i == 0:
        dp[i+1][0] = dp[i][0]+a
        dp[i+1][1] = dp[i][1]+b
        dp[i+1][2] = dp[i][2]+c
    else:
        dp[i+1][0] = max(dp[i][1]+a, dp[i][2]+a)
        dp[i+1][1] = max(dp[i][0]+b, dp[i][2]+b)
        dp[i+1][2] = max(dp[i][0]+c, dp[i][1]+c)

# print(dp,sep="\n")
print(max(dp[N][0],dp[N][1],dp[N][2]))
