N, Q = map(int, input().split())
C = list(map(int, input().split()))
for i in range(N):
    C[i] = set([C[i]])
ans = []
for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if len(C[a]) <= len(C[b]):
        for s in C[a]:
            C[b].add(s)
        C[a] = set()
    else:
        for s in C[b]:
            C[a].add(s)
        C[b] = set()
        C[a], C[b] = C[b], C[a]
    ans.append(len(C[b]))
print(*ans, sep="\n")
