class UnionFind:
    def __init__(self, n) -> None:
        self.par = [-1]*(n + 1)
        self.rank = [0]*(n + 1)

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        # 既に同じグループなら何もしない
        if x == y:
            return False

        # unionbysize
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return True

    def rank(self, x):
        return self.rank[x]
H,W=map(int,input().split())
Grid=[['.']*(W+2)]
for _ in range(H):
    Grid.append(['.']+list(input())+['.'])
Grid.append(['.']*(W+2))
UF=UnionFind((H+2)*(W+2))
dxy=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for i in range(1,H+1):
    for j in range(1,W+1):
        v=(W+2)*i + j
        if Grid[i][j]!='#':
            continue
        for di,dj in dxy:
            nv=(W+2)*(i+di)+j+dj
            if Grid[i+di][j+dj]!='#':
                continue
            UF.unite(v,nv)
ans=0
for x in range((H+2)*(W+2)):
    i=x//(W+2)
    j=x%(W+2)
    if Grid[i][j]=='#':
        if x==UF.root(x):
            ans+=1
print(ans)