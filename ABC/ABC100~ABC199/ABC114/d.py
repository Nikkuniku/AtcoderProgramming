from collections import Counter
n = int(input())
a = 1

divs = []
for i in range(2, n+1):
    j = 2
    while i > 1:
        if i % j == 0:
            i //= j
            divs.append(j)
        else:
            j += 1
c = Counter(divs)

ans = 0
# 1 素因数が74個
p = 0
for v in list(c.values()):
    if v >= 74:
        p += 1
ans += p
# 素因数が(2,24)
p = 0
q = 0
for v in list(c.values()):
    if v >= 2:
        q += 1
    if v >= 24:
        p += 1
ans += max((q-1), 0)*p
# 素因数が(4,14)
p = 0
q = 0
for v in list(c.values()):
    if v >= 4:
        q += 1
    if v >= 14:
        p += 1
ans += max((q-1), 0)*p

# 素因数が(2,2,4)
p = 0
q = 0
for v in list(c.values()):
    if v >= 2:
        q += 1
    if v >= 4:
        p += 1
ans += max((q-2), 0)*(p*(p-1)//2)
print(ans)
