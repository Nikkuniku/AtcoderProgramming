n,m=map(int,input().split())
edge=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)

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
u=UnionFind(n)

answer=[]
ans=0
points=set()
for v in range(n,1,-1):
    ans+=1
    points.add(v)
    for e in edge[v]:
        if e in points:
            if not u.issame(v,e):
                ans-=1
                u.unite(v,e)
    
    answer.append(ans)
answer=list(reversed(answer))
answer.append(0)
print(*answer,sep="\n")
