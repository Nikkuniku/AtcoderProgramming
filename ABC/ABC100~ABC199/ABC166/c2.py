N, M = map(int, input().split())
H = list(map(int, input().split()))
Edge = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)
ans = 0
for v in range(N):
    isOK = True
    for e in Edge[v]:
        if H[e] >= H[v]:
            isOK = False
    if isOK:
        ans += 1
print(ans)
