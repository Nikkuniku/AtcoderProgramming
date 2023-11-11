from collections import defaultdict

A = list(map(int, input().split()))
d = defaultdict(int)
for a in A:
    d[a] += 1
for i, v in d.items():
    if v == 1:
        exit(print(i))
