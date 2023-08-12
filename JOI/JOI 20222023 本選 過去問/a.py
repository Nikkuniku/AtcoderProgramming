from collections import defaultdict, deque
N = int(input())
d = defaultdict(lambda: 0)
A = []
stack = []
Edge = [[] for _ in range(N)]
ans = [-1]*N
for i in range(N):
    a = int(input())
    A.append(a)
    if d[a] > 0:
        while 1:
            color, idx = stack.pop()
            d[color] -= 1
            Edge[i].append(idx)
            Edge[idx].append(i)
            if color == a:
                break
    stack.append((a, i))
    d[a] += 1
for v in range(N-1, -1, -1):
    if ans[v] != -1:
        continue
    q = deque([v])
    c = A[v]
    ans[v] = c
    while q:
        v = q.popleft()
        for e in Edge[v]:
            if ans[e] != -1:
                continue
            ans[e] = c
            q.append(e)
print(*ans, sep="\n")
