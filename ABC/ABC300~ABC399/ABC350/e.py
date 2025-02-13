from collections import defaultdict
from collections import deque
from sys import setrecursionlimit

setrecursionlimit(10**8)
Edge_Y = defaultdict(set)
Edge_X = defaultdict(set)
N, A, X, Y = map(int, input().split())
seen = defaultdict(lambda: False)
q = deque([N])
seen[N] = True
while q:
    v = q.popleft()
    to = v // A
    Edge_X[to].add(v)
    if not seen[to]:
        seen[to] = True
        q.append(to)
    d = defaultdict(int)
    for b in range(2, 7):
        to = v // b
        d[to] += 1
    for to, val in d.items():
        Edge_Y[to].add((v, val))
        if not seen[to]:
            seen[to] = True
            q.append(to)
vals = sorted(set(list(Edge_X.keys()) + list(Edge_Y.keys())))[::-1]
INF = 1 << 60
dp = defaultdict(lambda: INF)
dp[N] = 0
for v in vals:
    # 操作1
    for e in Edge_X[v]:
        if v == e:
            continue
        dp[v] = min(dp[v], dp[e] + X)
    # 操作2
    tmp = Y / 5
    for e, cnt in Edge_Y[v]:
        if v == e:
            continue
        tmp += dp[e] * cnt / 5
        tmp += Y * cnt / 5
    dp[v] = min(dp[v], tmp)
print(dp[0])
