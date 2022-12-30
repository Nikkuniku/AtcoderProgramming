h,w=map(int,input().split())
grid=[]
for _ in range(h):
    grid.append(list(input()))

row=[]
col=[]
#行探索
for i in range(h):
    flg=0
    for j in range(w):
        if grid[i][j]=='#':
            flg=1

    if flg==0:
        row.append(i)

#列探索
for j in range(w):
    flg=0
    for i in range(h):
        if grid[i][j]=='#':
            flg=1

    if flg==0:
        col.append(j)

ans=[]
for i in range(h):
    arr=[]
    for j in range(w):
        if i in row or j in col:
            continue
        else:
            arr.append(grid[i][j])
    if len(arr)!=0:
        ans.append(arr)

for k in ans:
    t=''.join(k)
    print(t)
