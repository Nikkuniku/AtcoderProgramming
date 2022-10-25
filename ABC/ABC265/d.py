from collections import defaultdict
n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
csum = [0]
d = defaultdict(int)
for i in range(n):
    tmp = csum[-1]+a[i]
    csum.append(tmp)
    d[tmp] = i+1

for x in range(n+1):
    t1 = csum[x]+p
    y = d[t1]
    if y == 0:
        continue
    t2 = csum[y]+q
    z = d[t2]
    if z == 0:
        continue
    t3 = csum[z]+r
    w = d[t3]
    if w == 0:
        continue
    if x < y < z < w:
        print('Yes')
        exit()
print('No')
