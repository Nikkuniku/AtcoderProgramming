#####segfunc#####
from collections import defaultdict


def segfunc(x, y):
    return x+y
#################


#####ide_ele#####
ide_ele = 0
#################


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


H, W, N, h, w = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
d = defaultdict(int)
seg = SegTree([0]*302, segfunc, ide_ele)
for i in range(H):
    for j in range(W):
        d[A[i][j]] += 1
        seg.update(A[i][j], 1)

ans = [[0]*(W-w+1) for _ in range(H-h+1)]

for i in range(H-h+1):
    for j in range(W-w+1):
        if j == 0:
            for ni in range(h):
                for nj in range(w):
                    d[A[i+ni][j+nj]] -= 1
                    if d[A[i+ni][j+nj]] == 0:
                        seg.update(A[i+ni][j+nj], 0)

        else:
            for ni in range(h):
                d[A[i+ni][j+w-1]] -= 1
                if d[A[i+ni][j+w-1]] == 0:
                    seg.update(A[i+ni][j+w-1], 0)
        ans[i][j] = seg.query(0, 301)

        if j < W-w:
            for ni in range(h):
                d[A[i+ni][j]] += 1
                seg.update(A[i+ni][j], 1)
        else:
            for ni in range(h):
                for nj in range(w):
                    d[A[i+ni][j+nj]] += 1
                    seg.update(A[i+ni][j+nj], 1)

for c in ans:
    print(*c)
