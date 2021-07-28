h,w=map(int,input().split())
grid=[]
for _ in range(h):
    grid.append(list(map(int,input().split())))

ans=0
for i in range(1,1<<h):
    subgrid=[]
    for j in range(h):
        if (i>>j)&1:
            subgrid.append(grid[j])
    d={}
    for k in range(w):
        s=[r[k] for r in subgrid]
        if len(set(s))==1:
            if s[0] in d:
                d[s[0]]+=1
            else:
                d[s[0]]=1
    if list(d.values())==[]:
        tmp=0
    else:
        tmp=max(list(d.values()))
    
    ans=max(tmp*len(subgrid),ans)
print(ans)     