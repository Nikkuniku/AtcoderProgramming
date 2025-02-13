from atcoder.scc import SCCGraph

N = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))
g = SCCGraph(N)
for i in range(N):
    g.add_edge(i, A[i])
r = [0] * N
P = g.scc()[::-1]
for c in P:
    if len(c) > 1 or A[c[0]] == c[0]:
        for u in c:
            r[u] = len(c)
    else:
        r[c[0]] = r[A[c[0]]] + 1
print(sum(r))
