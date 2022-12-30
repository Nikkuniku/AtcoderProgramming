n, m = map(int, input().split())
edge = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)

for e in edge:
    print(*sorted(e))
