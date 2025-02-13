repuit = []
L = 20
tmp = 0
for i in range(L):
    tmp *= 10
    tmp += 1
    repuit.append(tmp)
N = int(input())
res = set()
for a in repuit:
    for b in repuit:
        for c in repuit:
            res.add(a + b + c)
res = list(res)
res.sort()
print(res[N - 1])
