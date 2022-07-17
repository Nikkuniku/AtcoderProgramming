from math import ceil
n = int(input())
d = 0
a = 0
b = 0
ans = []
for i in range(n):
    l, r = map(int, input().split())
    if i == 0:
        a = r
        b = l
        ans.append(d)
        continue
    p = max(l-a, b-r)
    if p > 2*d:
        d = ceil(p/2)
    a = min(a, r)
    b = max(b, l)
    ans.append(d)
print(*ans, sep="\n")
