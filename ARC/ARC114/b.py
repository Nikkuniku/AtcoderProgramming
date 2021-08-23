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

n=int(input())
mod=998244353
f=list(map(int,input().split()))
v=set(f)

uf = UnionFind(n)
for i in range(n):
    if i+1 in v:
        uf.unite(i+1,f[i])

cnt=0
for j in range(n):
    if j+1 not in v:
        continue
    if uf.root(j+1)==j+1:
        cnt+=1
ans=(pow(2,cnt,mod)-1)%mod

print(ans)