from sys import stdin
from math import factorial, sin
from collections import deque
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

n,m=map(int,stdin.readline().split())
edge=[]
for _ in range(m):
    a,b = map(int,stdin.readline().split())
    edge.append([a,b])

ans=factorial(n)//(factorial(2)*factorial(n-2))
answer=deque()
answer.appendleft(ans)
uf=UnionFind(n)
for i in range(m-1,0,-1):
    a = edge[i][0]
    b = edge[i][1]

    bf = uf.size[uf.root(a)]
    uf.unite(a,b)
    af = uf.size[uf.root(a)]
    
    ans-=(af - bf)*bf
    answer.appendleft(ans)

print(*answer,sep="\n")