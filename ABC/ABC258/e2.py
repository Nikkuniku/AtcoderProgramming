n, q, x = map(int, input().split())
w = list(map(int, input().split()))
C = [n*(x//sum(w))]*n
x = x % (sum(w))
Wdash = w+w
r = 0
s = 0
for le in range(n):
    if r < le:
        r = le
        s = 0

    while s < x:
        s += Wdash[r]
        r += 1

    C[le] += r-le
    s -= Wdash[le]
i = 0
roop = []
visited = set()
while True:
    roop.append(i)
    visited.add(i)
    i = (i+C[i]) % n
    if i in visited:
        break
for p, v in enumerate(roop):
    if v == i:
        break
cycle = roop[p:]
rooplen = len(cycle)
ans = []
for _ in range(q):
    k = int(input())
    k -= 1
    if k < len(roop):
        ans.append(C[roop[k]])
    else:
        k = (k-p) % rooplen
        ans.append(C[cycle[k]])
print(*ans, sep="\n")
