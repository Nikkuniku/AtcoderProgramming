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
Seg0 = SegTree([0]*(M+1), segfunc, ide_ele)
Seg1 = SegTree([INF]*(M+1), segfunc, ide_ele)
dp = [[[INF]*2 for _ in range(M)] for _ in range(N+1)]
for j in range(M):
    if j == 0:
        min0 = min(Seg0.query(1, M), Seg1.query(1, M))
    elif j == M-1:
        min0 = min(Seg0.query(0, M-1), Seg1.query(0, M-1))
    else:
        min0 = min(min(Seg0.query(0, j), Seg0.query(j+1, M)),
                   min(Seg1.query(0, j), Seg1.query(j+1, M)))
    for i in range(N):
        if i == 0:
            dp[i+1][j][0] = P[j][i]
            Seg0.update(j, P[j][i])
        else:
            dp[i+1][j][0] = min0+P[j][i]
            dp[i+1][j][1] = min(dp[i][j][0], dp[i][j][1])+P[j][i]-A
            Seg0.update(j, dp[i+1][j][0])
            Seg1.update(j, dp[i+1][j][1])

print(min(sum(dp[N], [])))
