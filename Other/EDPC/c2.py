n=int(input())
work=[]
for _ in range(n):
    work.append(list(map(int,input().split())))

dp=[[0]*3 for _ in range(n+1)]

for i in range(n):
    dp[i+1][0]=max(dp[i][1],dp[i][2])+work[i][0]
    dp[i+1][1]=max(dp[i][0],dp[i][2])+work[i][1]
    dp[i+1][2]=max(dp[i][0],dp[i][1])+work[i][2]

print(max(dp[n]))