#####segfunc#####
def segfunc(x, y):
    return min(x, y)
#################


#####ide_ele#####
ide_ele = 1 << 30
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


M, N, A = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(M)]
INF = 1 << 30
Seg = SegTree([INF]*(2*M+1), segfunc, ide_ele)
dp = [[[INF]*2 for _ in range(M)] for _ in range(N+1)]
for i in range(N):
    if i == 0:
        for j in range(M):
            p = P[j][i]
            dp[i+1][j][0] = p
            Seg.update(j, p)
    else:
        for j in range(M):
            p = P[j][i]
            min0 = min(Seg.query(0, j), Seg.query(j+1, M),
                       Seg.query(M, j+M), Seg.query(M+j+1, 2*M))
            dp[i+1][j][0] = min0+p
            dp[i+1][j][1] = min(dp[i][j][0], dp[i][j][1])+p-A
        for j in range(M):
            Seg.update(j, dp[i+1][j][0])
            Seg.update(j+M, dp[i+1][j][1])
ans = INF
for j in range(M):
    ans = min(ans, dp[N][j][0], dp[N][j][1])
print(ans)
