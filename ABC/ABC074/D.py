N=int(input())
grid=[]
grid2=[]
dist=[[float('inf')]*N for _ in range(N)]


for i in range(N):
    p=list(map(int,input().split()))
    grid.append(p)
    grid2.append(p)
    for j in [i-1,i,i+1]:
        if 0<=j<N:
            dist[i][j]=p[j]

print(grid)
print(grid2)

for k in range(N):
    for i in range(N):
        for j in range(N):
            grid2[i][j]=min(grid2[i][j],grid2[i][k]+grid2[k][j])

ans=-1
for p in range(N):
    for q in range(N):
        if grid[p][q]!=grid2[p][q]:
            print(ans)
            exit(0)
        
#Union Find
#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        tank = []
        while par[x] >= 0:
            tank.append(x)
            x = par[x]
        for elt in tank:
            par[elt] = x
        return x

#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]

#初期化
#根なら-size,子なら親の頂点
par = [-1]*N

edges=[]
for i in range(N):
    for j in range(i+1,N):
        edges.append((grid2[i][j],i,j))
    
edges=sorted(edges,key=lambda x: x[0])

ans=0
ans_e=[]
for k in range(len(edges)):
    e=edges[k]
    if same(e[1],e[2]):
        continue
    else:
        ans_e.append(e)
        ans+=e[0]
        unite(e[1],e[2])

print(ans)
print(ans_e)
    