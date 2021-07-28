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

import sys
n,m=map(int,sys.stdin.readline().split())

edge=[]
ans=0
for _  in range(m):
    a,b=map(int,sys.stdin.readline().split())
    edge.append([a,b])

for i in range(m):
    uf = UnionFind(n) 
    for j in range(m):
        if j==i:
            continue

        uf.unite(edge[j][0],edge[j][1])

    cnt=0
    for k in range(1,n+1):
        if uf.root(k)==k:
            cnt+=1

    if cnt>1:
        ans+=1

print(ans)