n=int(input())
a=list(map(int,input().split()))

arr=[]
for i in range(n//2):
    if a[i]!=a[n-1-i]:
        arr.append([a[i],a[n-1-i]])
from collections import Counter

c= Counter(a)

par = [-1 for i in range(n+1)]

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


print(par)

for j in range(len(arr)):
    p = arr[j]

    unite(p[0],p[1])

print(par)
