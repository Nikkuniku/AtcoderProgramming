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

n=int(input())
a=list(map(int,input().split()))
uf =UnionFind(max(a))

for i in range(n//2):
    uf.unite(a[i],a[n-1-i])    

ans=0
for i in range(len(uf.size)):
    if uf.root(i)==i:
        ans+=uf.size[i]-1

print(ans)

