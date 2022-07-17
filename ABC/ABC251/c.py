from collections import defaultdict
n = int(input())
judge = []
d = defaultdict(int)

for i in range(n):
    s, t = input().split()
    t = int(t)
    if s in d:
        continue
    d[s] = t
    judge.append((s, t, i))

maxvalue = max(list(d.values()))
for k, v, idx in judge:
    if v == maxvalue:
        break
print(idx+1)
