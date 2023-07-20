N, Q = map(int, input().split())
edge = [set() for _ in range(N)]
ans = N
res = []
for _ in range(Q):
    query = list(map(int, input().split()))
    q = query[0]
    if q == 1:
        u, v = query[1:]
        u -= 1
        v -= 1
        # どちらか一方
        if (edge[u] and not edge[v]) or (not edge[u] and edge[v]):
            ans -= 1
        # ともに空
        elif not edge[u] and not edge[v]:
            ans -= 2
        edge[u].add(v)
        edge[v].add(u)
    else:
        v = query[1]-1
        if edge[v]:
            while edge[v]:
                e = edge[v].pop()
                edge[e].discard(v)
                if not edge[e]:
                    ans += 1
            ans += 1
    res.append(ans)
print(*res, sep="\n")
