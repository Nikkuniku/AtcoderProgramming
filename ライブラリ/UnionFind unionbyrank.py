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

n,q=map(int,input().split())
u=UnionFind(n)

for _  in range(q):
    p,a,b=map(int,input().split())

    if p==0:
        u.unite(a,b)
    else:
        if u.issame(a,b):
            print('Yes')
        else:
            print('No')