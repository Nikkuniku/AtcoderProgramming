N, M, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    edge[u].append(v)
    edge[v].append(u)

C = list(map(int, input().split()))
ans = []
for _ in range(Q):
    query = list(map(int, input().split()))
    q = query[0]
    if q == 1:
        s = query[1]-1
        c = C[s]
        ans.append(c)
        for e in edge[s]:
            C[e] = c
    else:
        s, t = query[1:]
        s -= 1
        c = C[s]
        ans.append(c)
        C[s] = t

print(*ans, sep="\n")
