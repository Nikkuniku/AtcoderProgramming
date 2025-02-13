from math import gcd
from collections import defaultdict

L, R = map(int, input().split())
ans = 0
res = set()
d = defaultdict(list)
for x in range(L, R + 1):
    for y in range(L, R + 1):
        g = gcd(x, y)
        if g == 1:
            continue
        if x // g != 1 and y // g != 1:
            res.add((x, y))
            d[g].append((x, y))

print(len(res))
for k, v in d.items():
    print(k, len(v), v)
res = []
for x, y in d[2]:
    res.append((x // 2, y // 2))
# res.sort(key=lambda x: x[1])
# res.sort(key=lambda x: x[0])
print(res)
