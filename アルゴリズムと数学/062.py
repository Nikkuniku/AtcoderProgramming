n, k = map(int, input().split())
a = list(map(lambda x: int(x)-1, input().split()))

i = 0
s = set()
path = []
while True:
    s.add(i)
    path.append(i)

    i = a[i]
    if i in s:
        break
cycle = []
for m, v in enumerate(path):
    if v == i:
        break
cycle = path[m:]
rooplen = len(cycle)
if k < m:
    ans = path[k]
else:
    k -= m
    k = k % rooplen
    ans = cycle[k]
print(ans+1)
