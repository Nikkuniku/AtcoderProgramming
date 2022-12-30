N, M = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

for i in range(N):
    edge[i].sort()
    t = [p+1 for p in edge[i]]
    print(len(t), *t)
