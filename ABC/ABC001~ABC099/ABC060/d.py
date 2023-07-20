from collections import defaultdict
N, W = map(int, input().split())
goods = [list(map(int, input().split())) for _ in range(N)]
d = defaultdict(lambda: -1)
w1 = goods[0][0]
weights = set([0])
for k in range(1, N+1):
    for w in range(k*w1, k*(w1+3)+1):
        weights.add(w)
weights = sorted(list(weights))
d[(0, 0)] = 0
for i in range(N):
    wi, vi = goods[i]
    for w in weights:
        d[(i+1, w)] = d[(i, w)]
        if d[(i, w-wi)] != -1:
            d[(i+1, w)] = max(d[(i+1, w)], d[(i, w-wi)]+vi)
ans = -1
for k, w in list(d.keys()):
    if w <= W:
        ans = max(ans, d[(k, w)])
print(ans)
