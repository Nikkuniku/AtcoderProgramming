N = int(input())
from collections import defaultdict

INF = 1 << 60
d = defaultdict(lambda: INF)
for _ in range(N):
    a, c = map(int, input().split())
    d[c] = min(d[c], a)
ans = max(d.values())
print(ans)
