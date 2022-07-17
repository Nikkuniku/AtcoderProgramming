from collections import defaultdict
n, w = map(int, input().split())
a = list(map(int, input().split()))

d = defaultdict(int)
# 1個の時
for i in range(n):
    if a[i] > w:
        continue
    d[a[i]] = 1

# 2この時
for i in range(n):
    for j in range(i+1, n):
        if a[i]+a[j] > w:
            continue
        d[a[i]+a[j]] = 1
# 3この時
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if a[i]+a[j]+a[k] > w:
                continue
            d[a[i]+a[j]+a[k]] = 1

values = list(d.keys())
ans = 0
for v in values:
    if v <= w:
        ans += 1
print(ans)
