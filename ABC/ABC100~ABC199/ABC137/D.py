from heapq import heappush, heappop
N, M = map(int, input().split())
maxA = 10**5 + 1
INF = 1 << 30


class SegmentTree:
    def __init__(self, length, identity):
        self.length = length
        self.n_leaves = 2**length.bit_length()
        self.identity = identity
        self.value = [self.identity] * (2*self.n_leaves)
        self.index = [-1] * self.n_leaves + [i for i in range(self.n_leaves)]

    def func(self, x1, x2):
        return min(x1, x2), x1 <= x2

    def initialize(self, vector):
        self.value[self.n_leaves:self.n_leaves+len(vector)] = vector
        for i in range(self.n_leaves-1, 0, -1):
            value, flag = self.func(self.value[i*2], self.value[i*2+1])
            self.value[i] = value
            self.index[i] = self.index[i*2] if flag else self.index[i*2+1]

    def update(self, i, x, add=False):
        idx = self.n_leaves + i
        if add:
            self.value[idx] += x
        else:
            self.value[idx] = x
        while idx > 1:
            idx >>= 1
            value, flag = self.func(self.value[idx*2], self.value[idx*2+1])
            self.value[idx] = value
            self.index[idx] = self.index[idx *
                                         2] if flag else self.index[idx*2+1]

    # [i1, i2] (0-indexed)
    def query(self, i1=0, i2=-1):
        if i2 == -1:
            i2 += self.n_leaves
        idx1 = self.n_leaves + i1
        idx2 = self.n_leaves + i2
        answer = self.identity
        answer_idx = -1
        while idx1 <= idx2:
            if idx1 % 2 == 1:
                value, flag = self.func(answer, self.value[idx1])
                answer = value
                if not flag:
                    answer_idx = self.index[idx1]
                idx1 += 1
            if idx2 % 2 == 0:
                value, flag = self.func(answer, self.value[idx2])
                answer = value
                if not flag:
                    answer_idx = self.index[idx2]
                idx2 -= 1
            idx1 >>= 1
            idx2 >>= 1
        return answer, answer_idx


seg = SegmentTree(maxA+1, INF)
values = [[] for _ in range(maxA+1)]
for _ in range(N):
    a, b = map(int, input().split())
    heappush(values[a], -b)

for i in range(maxA+1):
    if values[i]:
        q = heappop(values[i])
        seg.update(i, q)
        heappush(values[i], q)
dp = [0]*(M+1)
for i in range(M-1, -1, -1):
    v, idx = seg.query(0, M-i)
    if idx == -1:
        dp[i] = dp[i+1]
        continue
    maxb = -heappop(values[idx])
    dp[i] = max(dp[i], dp[i+1]+maxb)

    if values[idx]:
        p = heappop(values[idx])
        seg.update(idx, p)
        heappush(values[idx], p)
    else:
        seg.update(idx, INF)

print(dp[0])
