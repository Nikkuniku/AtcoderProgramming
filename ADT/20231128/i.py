from itertools import product
from collections import defaultdict

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
P = list(product(range(2), repeat=N - 1))
route = [[] for _ in range(N)]
for p in P:
    i = sum(list(p))
    route[i].append(p)
ans = 0
for i in range(N):
    d_s = defaultdict(int)
    d_g = defaultdict(int)
    for path in route[i]:
        x, y = 0, 0
        tmp = A[x][y]
        for c in path:
            if c == 0:
                y += 1
            else:
                x += 1
            tmp ^= A[x][y]
        d_s[tmp] += 1

    for path in route[N - 1 - i]:
        x, y = N - 1, N - 1
        tmp = A[x][y]
        for c in path:
            if c == 0:
                y -= 1
            else:
                x -= 1
            tmp ^= A[x][y]
        tmp ^= A[x][y]
        d_g[tmp] += 1
    for k, v in d_g.items():
        ans += d_s[k] * v
print(ans)
