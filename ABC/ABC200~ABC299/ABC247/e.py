from collections import defaultdict
from bisect import bisect_left
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if a[i] < y or x < a[i]:
        b.append(i)
b.append(n)
r = 0
d = defaultdict(int)
ans = 0
for l in range(n):
    if a[l] < y or x < a[l]:
        continue
    while r < l:
        d[a[r]] -= 1
        r += 1

    while True:
        if min(d[x], d[y]) == 1:
            idx = bisect_left(b, r)
            ans += b[idx]-r+1
            break
        else:
            if r < n:
                if y <= a[r] <= x:
                    d[a[r]] += 1
                    r += 1
                else:
                    break
            else:
                break

    d[a[l]] -= 1
print(ans)
