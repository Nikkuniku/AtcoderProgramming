from sys import stdin
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

n,k,l=map(int,stdin.readline().split())

uf_road=UnionFind(n)
uf_railroad=UnionFind(n)
for _ in range(k):
    p,q=map(int,stdin.readline().split())
    uf_road.unite(p,q)
for _ in range(l):
    r,s=map(int,stdin.readline().split())
    uf_railroad.unite(r,s)

d={}
for i in range(1,n+1):
    a,b=uf_road.root(i),uf_railroad.root(i)
    if (a,b) in d:
        d[(a,b)]+=1
    else:
        d[(a,b)]=1

ans=[]
for j in range(1,n+1):
    a,b=uf_road.root(j),uf_railroad.root(j)
    ans.append(d[(a,b)])
print(*ans)
