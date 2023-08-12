from collections import defaultdict
from typing import Generic, Iterable, Iterator, List, Tuple, TypeVar, Optional
from bisect import bisect_left, bisect_right
import math


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


# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
T = TypeVar('T')


class SortedSet(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a: Optional[List[T]] = None) -> None:
        "Evenly divide `a` into buckets."
        if a is None:
            a = list(self)
        size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size: size *
                    (i + 1) // bucket_size] for i in range(bucket_size)]

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        self.size = len(a)
        if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
            a = sorted(set(a))
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i):
                yield j

    def __eq__(self, other) -> bool:
        return list(self) == list(other)

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1: len(s) - 1] + "}"

    def _position(self, x: T) -> Tuple[List[T], int]:
        "Find the bucket and position which x should be inserted. self must not be empty."
        for a in self.a:
            if x <= a[-1]:
                break
        return (a, bisect_left(a, x))

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        a, i = self._position(x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a, i = self._position(x)
        if i != len(a) and a[i] == x:
            return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()
        return True

    def _pop(self, a: List[T], i: int) -> T:
        ans = a.pop(i)
        self.size -= 1
        if not a:
            self._build()
        return ans

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        a, i = self._position(x)
        if i == len(a) or a[i] != x:
            return False
        self._pop(a, i)
        return True

    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, i: int) -> T:
        "Return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0:
                    return a[i]
        else:
            for a in self.a:
                if i < len(a):
                    return a[i]
                i -= len(a)
        raise IndexError

    def pop(self, i: int = -1) -> T:
        "Pop and return the i-th element."
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0:
                    return self._pop(a, i)
        else:
            for a in self.a:
                if i < len(a):
                    return self._pop(a, i)
                i -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


N = int(input())
info = [input().split() for _ in range(N)]
Q = int(input())
query = [input().split() for _ in range(Q)]
# 座圧
S = set()
for _, l, r in info:
    S.add(int(l))
    S.add(int(r))
for i in range(Q):
    t, *q = query[i]
    if t == '1':
        S.add(int(q[1]))
    if t == '2':
        S.add(int(q[0]))
    if t == '3':
        _, l, r = q
        S.add(int(l))
        S.add(int(r))
compress = defaultdict(int)
for i, v in enumerate(sorted(list(S))):
    compress[v] = i
compress_info = []
L_user = defaultdict(SortedSet)
R_user = defaultdict(int)
Seg = SegTree([0]*(max(compress.values())+1), segfunc, 0)
for x, l, r in info:
    L = compress[int(l)]
    R = compress[int(r)]
    L_user[x].add(L)
    R_user[x, L] = R
    Seg.add(L, 1)
    Seg.add(R+1, -1)
ans = []
for i in range(Q):
    t, *q = query[i]
    t = int(t)
    if t == 1:
        x, t = q
        t = compress[int(t)]
        L = L_user[x].le(t)
        res = 'No'
        if L != None:
            R = R_user[x, L]
            if L <= t <= R:
                res = 'Yes'
        ans.append(res)
    elif t == 2:
        t = compress[int(q[0])]
        t2 = Seg.query(0, t+1)
        ans.append(t2)
    elif t == 3:
        x, l, r = q
        L = compress[int(l)]
        R = compress[int(r)]
        L_user[x].add(L)
        R_user[x, L] = R
        Seg.add(L, 1)
        Seg.add(R+1, -1)
print(*ans, sep="\n")
