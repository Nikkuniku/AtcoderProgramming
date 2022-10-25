from collections import defaultdict
n = int(input())
a = list(map(int, input().split()))
b = list(set(a))
b.sort()
d = defaultdict(int)
for i, v in enumerate(b):
    d[v] = i+1
for i in range(n):
    a[i] = d[a[i]]
print(*a)
