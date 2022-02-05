h,w=map(int,input().split())
grid=[]
for _ in range(h):
    grid.append(list(input()))

dp=[[0]*w for _ in range(h)]
can=[[False]*w for _ in range(h)]
can[0][0]=True
dp[0][0]=1

dx=[0,1]
dy=[1,0]
for i in range(h):
    for j in range(w):
        if grid[i][j]=='.' and can[i][j]:
            for k in range(2):
                ny = i+dy[k]
                nx = j+dx[k]
                if 0<=ny<h and 0<=nx<w:
                    if grid[ny][nx]=='.':
                        can[ny][nx]=True
                        dp[ny][nx]=dp[i][j]+1
           
ans=0
for i in range(h):
    for j in range(w):
        if can[i][j]:
            ans= max(ans,dp[i][j])
print(ans)