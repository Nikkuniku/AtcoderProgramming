n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
ans = 0
for a in range(n):
    for b in range(a+1, n):
        for c in range(b+1, n):
            if (b in edge[a] and a in edge[b]) and (b in edge[c] and c in edge[b]) and (c in edge[a] and a in edge[c]):
                ans += 1
print(ans)
