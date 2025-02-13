N = int(input())
repunits = []
t = 0
for _ in range(50):
    t = 10 * t + 1
    repunits.append(t)
res = set()
M = len(repunits)
for i in range(M):
    for j in range(M):
        for k in range(M):
            p = repunits[i] + repunits[j] + repunits[k]
            res.add(p)
res = sorted(res)
print(res[N - 1])
