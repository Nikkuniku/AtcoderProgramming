from collections import Counter
from math import ceil
from collections import deque
from random import randint, choice


class UnionFind:
    def __init__(self, n) -> None:
        self.par = [-1]*(n + 1)
        self.size = [1]*(n + 1)

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


N, M, D, K = map(int, input().split())
Edge = []
for i in range(M):
    u, v, w = map(int, input().split())
    Edge.append((i, u, v, w))
for _ in range(N):
    x, y = map(int, input().split())
Edge.sort(key=lambda x: x[3])
did = [False]*M
ans = [-1]*M


def check(A, P):
    pass
    if (D*A + (D*(D-1)*p)//2) != M:
        return False
    if A+(D-1)*P > K:
        return False
    return True


wariate = []
for a in range(K+1):
    for p in range(K+1):
        if check(a, p):
            wariate.append((a, p))
wariate.sort(key=lambda x: x[1])
can = []
for a, p in wariate:
    tmp = []
    for d in range(D):
        tmp.append(a+d*p)
    can.append(tmp)
arr = []
cnt = M
for _ in range(D):
    arr.append(min(max(cnt, 0), K))
    cnt -= K
if can:
    arr = can[-1][::-1]

for d in range(D):
    # 頂点集合作成
    UF = UnionFind(N)
    # 既に工事済みの辺はくっつける
    for i, u, v, w in Edge:
        if did[i]:
            UF.unite(u, v)
    kouji = []
    # 最小全域木の要領で工事しても良い辺を見つける
    for i, u, v, w in Edge:
        if UF.issame(u, v):
            kouji.append((i, u, v, w))
            continue
        UF.unite(u, v)
    # 重みが大きい順に工事したいのでソートする
    kouji.sort(key=lambda x: x[3])
    # 工事数
    cnt = 0
    flg = True
    q = deque(kouji)
    while cnt < arr[d]:
        if flg:
            if q:
                i, u, v, w = q.popleft()
                # 既に工事済みなら何もしない
                if did[i]:
                    continue
                # 工事したことないなら工事する。
                ans[i] = d+1
                did[i] = True
        else:
            if q:
                i, u, v, w = q.pop()
                # 既に工事済みなら何もしない
                if did[i]:
                    continue
                # 工事したことないなら工事する。
                ans[i] = d+1
                did[i] = True
        cnt += 1
        flg = not flg
for i in range(M):
    if ans[i] == -1:
        ans[i] = D
print('--')
print(*ans)
print('--')
print(Counter(ans))
print(arr)
print(sum(arr))
