from heapq import heappop
from collections import defaultdict

Q = int(input())
V = [-1] * (Q + 1)
prev = [-1] * (Q + 1)
prev[0] = 0
v = 0
ans = []
next = [i for i in range(1, Q + 1)]
d = defaultdict(int)
for _ in range(Q):
    query = input().split()
    t = query[0]
    if t == "ADD":
        x = int(query[1])
        y = heappop(next)
        prev[y] = v
        V[y] = x
        v = y
    elif t == "DELETE":
        v = prev[v]
    elif t == "SAVE":
        y = int(query[1])
        d[y] = v
    elif t == "LOAD":
        z = int(query[1])
        v = d[z]
    ans.append(V[v])
print(*ans)
