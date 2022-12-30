h,w=map(int,input().split())
grid=[]
for _ in range(h):
    grid.append(list(input()))

dp=[[0]*(w+1) for _ in range(h+1)]

for i in range(h-1,-1,-1):
    for j in range(w-1,-1,-1):
        if grid[i][j]=='#':
            continue
        dp[i][j]=max(dp[i+1][j],dp[i][j+1])+1

ans=dp[0][0]
print(ans)
