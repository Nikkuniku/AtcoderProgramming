from copy import deepcopy
from tokenize import ContStr


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
cost = deepcopy(a)

for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])

if a != cost:
    print(-1)
    exit()

ans = 0
edge = set()
for k in range(n):
    for i in range(n):
        for j in range(i+1, n):
            if cost[i][j] == cost[i][k]+cost[k][j]:
                edge.add((i, k))
                edge.add((k, j))

for u, v in edge:
    ans += cost[u][v]
print(ans)
