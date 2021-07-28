from sys import stdin
from collections import deque
from typing import Union
n,m=map(int, stdin.readline().split())
edge=[[]for _ in range(n+1)]

A=[0]+list(map(int,input().split()))
B=[0]+list(map(int,input().split()))
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

u=UnionFind(n)

for _ in range(m):
    a,b=map(int, stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)
    u.unite(a,b)
# 根を求める
roots=[]
for i in range(1,n+1):
    if u.root(i)==i:
        roots.append(i)

dist=[-1]*(n+1)
ans='Yes'
for v in roots:
    q=deque([v])
    dist[v]=0
    tmp=B[v]-A[v]

    while q:
        v=q.popleft()

        for e in edge[v]:
            if dist[e]==-1:
                dist[e]=dist[v]+1
                tmp+=(B[e]-A[e])
                q.append(e)

    if tmp!=0:
        ans='No'
        break
print(ans)