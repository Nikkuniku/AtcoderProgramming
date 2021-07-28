dx=[0,1,0,-1]
dy=[1,0,-1,0]

d={}
cnt=0
def dfs(x,y,cnt):
    if cnt==k:
        

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        dfs(nx,ny,cnt+1)