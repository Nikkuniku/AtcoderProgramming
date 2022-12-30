N = int(input())
S = list(input())
Q = int(input())


def segfunc(x, y):
    return max(x, y)
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


Forest = [SegTree([0]*(N+1), segfunc, ide_ele) for _ in range(26)]
ans = []


def alpindex(s):
    return ord(s)-97


for i in range(N):
    idx = alpindex(S[i])
    Forest[idx].update(i+1, 1)

for _ in range(Q):
    query = list(input().split())
    q = int(query[0])
    if q == 1:
        s, t = int(query[1]), query[2]
        if S[s-1] == t:
            continue
        idx = alpindex(S[s-1])
        Forest[idx].update(s, 0)
        Forest[alpindex(t)].update(s, 1)
        S[s-1] = t
    else:
        s, t = int(query[1]), int(query[2])
        tmp = 0
        for i in range(26):
            tmp += Forest[i].query(s, t+1)
        ans.append(tmp)
print(*ans, sep="\n")
