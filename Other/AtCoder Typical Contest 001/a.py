import sys
sys.setrecursionlimit(10**7) #再帰関数の呼び出し制限
h,w=map(int,input().split())
grid=[]
grid.append(['#']*(w+2))
for i in range(h):
    g=['#']+list(input())+['#']
    grid.append(g)
    if 's' in g:
        sx=i+1
        sy=g.index('s')
    if 'g' in g:
        gx=i+1
        gy=g.index('g')
grid.append(['#']*(w+2))
reached=[[False]*(w+2) for _ in range(h+2)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def dfs(x,y):
    if grid[x][y]=='#':
        return
    if reached[x][y]:
        return
    reached[x][y]=True

    for i in range(4):
        dfs(x+dx[i],y+dy[i])
dfs(sx,sy)
ans='No'
if reached[gx][gy]:
    ans='Yes'
print(ans)