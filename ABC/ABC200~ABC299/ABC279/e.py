from collections import defaultdict
N, M = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))
S = [i for i in range(N)]
G = [i for i in range(N)]
d = defaultdict(lambda: -1)
for i in range(N):
    d[i] = i
for i in range(M-1, 0, -1):
    a = A[i]
    x, y = a, a+1
    G[x], G[y] = G[y], G[x]
ans = []
for i in range(M):
    res = -1
    if i == 0:
        res = G[0]
    elif i == M-1:
        res = S[0]
    else:
        res = G[S[0]]
    x, y = d[A[i]], d[A[i]+1]
    d[A[i]], d[A[i]+1] = y, x
    S[x], S[y] = S[y], S[x]
    if i < M-1:
        v, w = A[i+1], A[i+1]+1
        G[v], G[w] = G[w], G[v]
    ans.append(res+1)
print(*ans, sep="\n")
