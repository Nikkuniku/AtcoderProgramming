n,m=map(int,input().split())
node=[[] for _ in range(n+1)]
edge=set()

class UnionFind:
    def __init__(self,n) -> None:
        self.par=[-1]*(n + 1)
        self.size=[1]*(n + 1)

    def root(self,x):
        if self.par[x]==-1:
            return x
        else: 
            self.par[x]=self.root(self.par[x])
            return self.par[x]

    def issame(self,x,y):
        return self.root(x)==self.root(y)
    
    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)

        # 既に同じグループなら何もしない
        if x==y:
            return False
        
        # unionbysize
        if self.size[x]<self.size[y]:
            x , y = y , x

        self.par[y] =x
        self.size[x] += self.size[y]
        
        return True
    
    def issize(self,x):
        return self.size[self.root(x)]

uf = UnionFind(n)

for _ in range(m):
    a,b=map(int,input().split())
    edge.add((a,b))

ans='Yes'
edge=list(edge)
for i in range(len(edge)):
    e=edge[i]
    a=e[0]
    b=e[1]
    node[a].append(b)
    node[b].append(a)

    if uf.issame(a,b):
        ans='No'
        break
    else:
        uf.unite(a,b)

for i in range(1,n+1):
    if len(node[i])>2:
        ans='No'
        break

print(ans)