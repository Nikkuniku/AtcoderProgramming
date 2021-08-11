from bisect import bisect_right
n, k, p = map(int, input().split())

a = list(map(int, input().split()))
b = a[:n//2]
c = a[n//2:]
x = [[] for _ in range(n//2 + 1)]
y = [[] for _ in range(n - n//2 + 1)]
for i in range(1 << n//2):
    cnt = 0
    total = 0
    for j in range(n//2):
        if (i >> j) & 1:
            total += b[j]
            cnt += 1
    x[cnt].append(total)
for i in range(1 << n - n//2):
    cnt = 0
    total = 0
    for j in range(n - n//2):
        if (i >> j) & 1:
            total += c[j]
            cnt += 1
    y[cnt].append(total)

for l in range(len(y)):
    y[l] = sorted(y[l])
ans = 0
for i in range(n//2 + 1):
    r = x[i]
    if k-i >= len(y):
        continue
    for q in r:
        if p-q < 0:
            continue
        result = bisect_right(y[k-i], p-q)
        ans += result

print(ans)
