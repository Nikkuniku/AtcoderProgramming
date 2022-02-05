h,w=map(int,input().split())
grid=[]
for _ in range(h):
    grid.append(list(map(int,input().split())))

horizon=[]
for i in range(h):
    horizon.append(sum(grid[i]))

vertial = [sum(column) for column in zip(*grid)]

ans=[[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans[i][j]=horizon[i]+vertial[j]-grid[i][j]

for c in ans:
    print(*c)