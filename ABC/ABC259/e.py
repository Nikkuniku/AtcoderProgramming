from collections import defaultdict
n = int(input())
a = []

d = defaultdict(list)
s = set()
for i in range(n):
    m = int(input())
    tmp = []
    for i in range(m):
        p, e = map(int, input().split())
        d[p].append(e)
        s.add(p)
        tmp.append((p, e))
    a.append(tmp)

t = []
idx = defaultdict(int)
i = 0
for p in s:
    d[p].append(0)
    d[p].sort()
    d[p] = d[p][-2:]
    idx[p] = i
    t.append(d[p][-1])
    i += 1

ans = set()

for i in range(n):
    p = a[i]
    for q in p:
        x, y = q
        j = idx[x]
        if t[j] == y:
            t[j] = d[x][0]
    ans.add(tuple(t))
    for q in p:
        x, y = q
        j = idx[x]
        t[j] = d[x][-1]

print(len(ans))
