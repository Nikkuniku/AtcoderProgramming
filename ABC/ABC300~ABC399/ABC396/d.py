from itertools import permutations
from collections import defaultdict

Edge = defaultdict(lambda: -1)
N, M = map(int, input().split())
for _ in range(M):
    u, v, w = map(int, input().split())
    if v < u:
        u, v = v, u
    Edge[u, v] = w
ans = 1 << 60
for c in range(N - 2 + 1):
    P = list(permutations([i for i in range(2, N)], c))
    for p in P:
        path = [1]
        for j in p:
            path.append(j)
        path.append(N)
        temp = 0
        isOK = True
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            if v < u:
                u, v = v, u
            if Edge[u, v] == -1:
                isOK = False
                break
            temp ^= Edge[u, v]
        if isOK:
            ans = min(ans, temp)
print(ans)
