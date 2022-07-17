from itertools import groupby
s = input()
t = input()
grs = groupby(s)
grt = groupby(t)
rans = []
rant = []
for k, v in grs:
    rans.append((k, len(list(v))))
for k, v in grt:
    rant.append((k, len(list(v))))

ans = 'Yes'
if len(rans) != len(rant):
    ans = 'No'
    print(ans)
    exit()

for i in range(len(rans)):
    p = rans[i]
    q = rant[i]
    if p[0] != q[0]:
        ans = 'No'
        break
    if p[1] >= 2 and q[1] >= p[1]:
        continue
    elif p[1] == 1 and q[1] == 1:
        continue
    else:
        ans = 'No'
        break

print(ans)
