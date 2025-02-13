from string import ascii_uppercase
from collections import defaultdict


class UnionFind:
    def __init__(self) -> None:
        self.par = defaultdict(lambda: -1)
        self.size = defaultdict(lambda: 1)

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
        if self.size[x] < self.size[y]:
            x, y = y, x

        self.par[y] = x
        self.size[x] += self.size[y]

        return True

    def issize(self, x):
        return self.size[self.root(x)]

    def groups(self) -> list:
        """
        グループ構造の詳細を返す

        Return
        ------
        res:list[]
            グループ構造を返す
        """
        member = [[] for _ in range(len(self.par))]
        for v in range(len(self.par)):
            member[self.root(v)].append(v)
        res = []
        for mem in member:
            if mem:
                res.append(mem)
        return res


UF = UnionFind()
N = int(input())
s1 = input()
s2 = input()
d = defaultdict(lambda: -1)
for i in range(N):
    t1 = s1[i]
    t2 = s2[i]
    if t1 in ascii_uppercase and t2 in ascii_uppercase:
        UF.unite(t1, t2)
        if i == 0:
            UF.unite(t1, "0")
    if t1 in ascii_uppercase and t2 not in ascii_uppercase:
        d[t1] = int(t2)
    if t1 not in ascii_uppercase and t2 in ascii_uppercase:
        d[t2] = int(t1)
groups = defaultdict(list)
for k in list(UF.par.keys()):
    groups[UF.root(k)].append(k)
e = defaultdict(int)
for k, v in groups.items():
    groups_tmp = "".join(list(v))
    num = max([d[p] for p in v])
    e[groups_tmp] = num
ans = 1
for k, v in e.items():
    if v > -1:
        continue
    if "0" in k:
        ans *= 9
    else:
        ans *= 10
print(ans)
