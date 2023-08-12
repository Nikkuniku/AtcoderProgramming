def segfunc(x, y):
    return x+y


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])

    def add(self, k, x):
        k += self.num
        self.tree[k] += x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r-1])
            l >>= 1
            r >>= 1
        return res


N, Q, S, T = map(int, input().split())
A = [int(input()) for _ in range(N+1)]+[0]
CUMSUM = [0]*(N+2)
Seg = SegTree(CUMSUM, segfunc, 0)

res = 0
for i in range(N):
    w = abs(A[i]-A[i+1])
    if A[i] < A[i+1]:
        w *= -S
    else:
        w *= T
    res += w
ans = [res]
for _ in range(Q):
    L, R, X = map(int, input().split())
    tmp1 = 0
    tmp2 = 0
    # 区間の端点が変化量なので、注目する
    a_L = A[L-1]+Seg.query(0, L)
    a_R = A[L]+Seg.query(0, L+1)
    if a_L < a_R:
        tmp1 -= abs(a_L-a_R)*S
    else:
        tmp1 += abs(a_L-a_R)*T
    b_L = A[R]+Seg.query(0, R+1)
    b_R = A[min(R+1, N)]+Seg.query(0, min(R+1+1, N+1))
    if b_L < b_R:
        tmp2 -= abs(b_L-b_R)*S
    else:
        tmp2 += abs(b_L-b_R)*T
    # imosのように区間端に足す
    s = Seg.query(L, L+1)
    t = Seg.query(R+1, R+1+1)
    Seg.update(L, s+X)
    Seg.update(R+1, t-X)
    tmp1 *= -1
    tmp2 *= -1
    a_L = A[L-1]+Seg.query(0, L)
    a_R = A[L]+Seg.query(0, L+1)
    if a_L < a_R:
        tmp1 -= abs(a_L-a_R)*S
    else:
        tmp1 += abs(a_L-a_R)*T
    b_L = A[R]+Seg.query(0, R+1)
    b_R = A[min(R+1, N)]+Seg.query(0, min(R+1+1, N+1))
    if b_L < b_R:
        tmp2 -= abs(b_L-b_R)*S
    else:
        tmp2 += abs(b_L-b_R)*T
    diff = tmp1+tmp2
    ans.append(ans[-1]+diff)
print(*ans[1:], sep="\n")
