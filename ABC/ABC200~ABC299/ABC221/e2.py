from collections import defaultdict


class BIT:
    # 長さN+1の配列を初期化
    def __init__(self, N):
        self.size = N
        self.bit = [0] * (N + 1)

    # i番目までの和を求める
    def sum(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]  # フェニック木のi番目の値を加算
            i -= -i & i  # 最も右にある1の桁を0にする
        return res

    # i番目の値にxを足して更新する
    def add(self, i, x):
        while i <= self.size:
            self.bit[i] += x  # フェニック木のi番目にxを足して更新
            i += -i & i  # 最も右にある1の桁に1を足す


N = int(input())
A = list(map(int, input().split()))
B = sorted(set(A))
d = defaultdict(int)
for i, v in enumerate(B, 1):
    d[v] = i
C = [d[a] for a in A]
M = len(C)
P = max(C)
FenwickTree = BIT(P)
ans = 0
MOD = 998244353
for j in range(M):
    cj = C[j]
    b = FenwickTree.sum(cj)
    tmp = pow(2, j, MOD) * b
    ans += tmp
    ans %= MOD
    FenwickTree.add(cj, pow(2, -(j + 1), MOD))
print(ans)
