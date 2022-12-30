from typing import Union


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
    
    def size(self,x):
        return self.size[x]

n,m,k=map(int,input().split())
uf=UnionFind(n)
candidate=[0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    candidate[a]-=1
    candidate[b]-=1
    uf.unite(a,b)

for i in range(1,n+1):
    candidate[i]+=uf.size[uf.root(i)]-1

for _ in range(k):
    c,d=map(int,input().split())
    if uf.issame(c,d):
        candidate[c]-=1
        candidate[d]-=1

print(*candidate[1:])