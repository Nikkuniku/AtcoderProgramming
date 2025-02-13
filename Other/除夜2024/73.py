from collections import defaultdict

N = int(input())
d = defaultdict(list)
for _ in range(N):
    a, c = map(int, input().split())
    d[c].append(a)
res = []
for k, v in d.items():
    res.append(min(v))
print(max(res))
