from itertools import groupby
n = int(input())
ca = [0]*367
days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(1, len(days)):
    days[i] += days[i-1]
i = 1
while i < 367:
    ca[i] = 1
    i += 7
j = 7
while j < 367:
    ca[j] = 1
    j += 7
for _ in range(n):
    m, d = map(int, input().split('/'))
    p = days[m-1]+d
    while p < 367:
        if ca[p] == 0:
            ca[p] = 1
            break
        else:
            p += 1
gr = groupby(ca)
ans = 0
for key, value in gr:
    if key == 1:
        ans = max(ans, len(list(value)))
print(ans)
