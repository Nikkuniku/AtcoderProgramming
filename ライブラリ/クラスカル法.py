class UnionFind:
    def __init__(self,n) -> None:
        self.par = [-1]*(n + 1)
        self.rank = [0]*(n + 1)

    def root(self,x):
        if self.par[x] == -1:
            return x
        else: 
            self.par[x]=self.root(self.par[x])
            return self.par[x]

    def issame(self,x,y):
        return self.root(x) == self.root(y)
    
    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)

        # 既に同じグループなら何もしない
        if x==y:
            return False
        
        # unionbysize
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return True
    
    def rank(self,x):
        return self.rank[x]

V,E=map(int,input().split())
uf=UnionFind(V)
Edge=[]
for i in range(E):
    s,t,w=map(int,input().split())
    Edge.append((s,t,w,i))

Edge.sort(key=lambda x:abs(x[2]))
ans=0
selected=set()
for e in Edge:
    s,t,w,i=e
    if not uf.issame(s,t):
        uf.unite(s,t)
        selected.add(i)

ans=0
for e in Edge:
    s,t,w,i=e
    if not i in selected:
        ans+=w
print(ans)