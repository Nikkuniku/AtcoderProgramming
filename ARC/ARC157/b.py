from itertools import groupby
import heapq


class Reverse:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __repr__(self):
        return repr(self.val)


class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            for i in range(len(arr)):
                arr[i] = Reverse(arr[i])
        self.desc = desc
        self.hq = arr
        heapq.heapify(self.hq)

    def pop(self):
        if self.desc:
            return heapq.heappop(self.hq).val
        else:
            return heapq.heappop(self.hq)

    def push(self, a):
        if self.desc:
            heapq.heappush(self.hq, Reverse(a))
        else:
            heapq.heappush(self.hq, a)

    def top(self):
        if self.desc:
            self.hq[0].val
        else:
            return self.hq[0]


N, K = map(int, input().split())
S = input()
if S.count('Y') == 0:
    print(K-1)
    exit()
q = Heapq([], True)
seen = [False]*N
val = [0]*N
for i in range(N):
    if i == 0:
        if S[i] == 'X':
            if S[i+1] == 'Y':
                val[i] += 1
                q.push((1, i))
        else:
            if S[i+1] == 'Y':
                val[i] -= 1
                q.push(-1, i)
    elif i == N-1:
        if S[i] == 'X':
            if S[i-1] == 'Y':
                val[i] += 1
                q.push((1, i))
        else:
            if S[i-1] == 'Y':
                val[i] -= 1
                q.push((-1, i))
    else:
        if S[i] == 'X':
            for j in [-1, 1]:
                if S[i] != S[i+j]:
                    val[i] += 1
            if val[i] == 2:
                q.push((2, i))
        else:
            for j in [-1, 1]:
                if S[i] == S[i+j]:
                    val[i] -= 1
            if val[i] == -2:
                q.push((-2, i))

ans = list(S)
for _ in range(K):
    v, i = q.pop()
    seen[i] = True
    if S[i] == 'X':
        for j in [-1, 1]:
            if 0 <= i+j < N:
                if S[i] == S[i+j]:
                    val[i+j] += 1
                    if not seen[i+j]:
                        q.push((val[i+j], i+j))
                else:
                    val[i+j] -= 1
                    if val[i+j] == -2 and not seen[i+j]:
                        q.push((val[i+j], i+j))
        ans[i] = 'Y'
    else:
        for j in [-1, 1]:
            if 0 <= i+j < N:
                if S[i] == S[i+j]:
                    val[i+j] += 1
                    q.push((val[i+j], i+j))
                else:
                    val[i+j] -= 1
                    q.push((val[i+j], i+j))
        ans[i] = 'X'

gr = groupby(''.join(ans))
res = 0
for k, v in gr:
    if k == 'Y':
        res += len(list(v))-1
print(res)
