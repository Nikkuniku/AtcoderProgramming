from itertools import groupby
n = int(input())
s = list(input())

gr = groupby(s)
vs = []
for k, v in gr:
    t = list(v)
    vs.append(len(t))

ans = 0
for v in vs:
    ans += v*(v-1)//2
print(ans)
