n=int(input())
h,w=1005,1005
grid=[[0]*w for _ in range(h)]

for _ in range(n):
    lx,ly,rx,ry=map(int,input().split())
    
    grid[ly][lx]+=1
    grid[ry][rx]+=1
    grid[ly][rx]-=1
    grid[ry][lx]-=1

for i in range(h):
    for j in range(1,w):
        grid[i][j]+=grid[i][j-1]

for i in range(1,h):
    for j in range(w):
        grid[i][j]+=grid[i-1][j]

ans=[0]*(n+1)
for i in range(h):
    for j in range(w):
        ans[grid[i][j]]+=1

for k in range(n):
    print(ans[k+1])