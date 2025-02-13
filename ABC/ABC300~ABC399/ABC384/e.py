class UnionFind:
    def __init__(self, n) -> None:
        """
        初期化

        Parameters
        ----------
        n:要素数
        """
        self.par = [-1] * (n + 1)
        self.size = [1] * (n + 1)

    def root(self, x) -> int:
        """
        xの属するグループの親番号を返す

        Parameters
        ----------
        x:要素番号

        Return
        ------
        res:int
            xの属するグループの親番号
        """
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def issame(self, x, y) -> bool:
        """
        xとyが同じグループに属するかどうかを返す

        Parameters
        ----------
        x,y:要素番号

        Return
        ------
        res:bool
            true:xとyは同じグループである
            false:xとyは同じグループでない
        """
        return self.root(x) == self.root(y)

    def unite(self, x, y) -> bool:
        """
        xの属するグループとyの属するグループを併合する

        Parameters
        ----------
        x,y:要素番号

        Return
        ------
        res:bool
            true:xとy、それぞれの属するグループを併合する
            false:xとyはすでに同じグループのため、併合は行わない
        """
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

    def issize(self, x) -> int:
        """
        xの属するグループのサイズを返す

        Return
        ------
        res:int
            xの属するグループのサイズ
        """
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


from heapq import heappop, heappush

H, W, X = map(int, input().split())
P, Q = map(int, input().split())
P -= 1
Q -= 1
S = [list(map(int, input().split())) for _ in range(H)]
UF = UnionFind(H * W)


def mapping(i, j):
    return W * i + j


heap = []
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
seen = set([(P, Q)])
Now = S[P][Q]
for dx, dy in dxy:
    nx = P + dx
    ny = Q + dy
    if not (0 <= nx < H and 0 <= ny < W):
        continue
    heappush(heap, (S[nx][ny], nx, ny))
    seen.add((nx, ny))
slime = mapping(P, Q)
while heap:
    t, wx, wy = heappop(heap)
    if X * t >= Now:
        break
    target = mapping(wx, wy)
    if UF.issame(slime, target):
        continue
    UF.unite(slime, target)
    Now += t
    for dx, dy in dxy:
        nx = wx + dx
        ny = wy + dy
        next_target = mapping(nx, ny)
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        if UF.issame(slime, next_target):
            continue
        if (nx, ny) in seen:
            continue
        heappush(heap, (S[nx][ny], nx, ny))
        seen.add((nx, ny))
print(Now)
