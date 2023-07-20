from collections import deque
N, K = map(int, input().split())
MOD = 10**9+7
ans = K
Edge = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    Edge[a].append(b)
    Edge[b].append(a)
q = deque([0])
seen = [False]*N
while q:
    v = q.popleft()
    seen[v] = True
    i = 0
    if v != 0:
        i += 1
    for e in Edge[v]:
        if seen[e]:
            continue
        i += 1
        ans = ans*(K-i) % MOD
        q.append(e)
print(ans)
