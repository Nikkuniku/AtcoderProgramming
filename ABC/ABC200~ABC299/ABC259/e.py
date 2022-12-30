from collections import defaultdict
n = int(input())
A = []

d = defaultdict(list)
primecnt = defaultdict(int)
LCM = defaultdict(int)
s = set()
for i in range(n):
    m = int(input())
    tmp = []
    for i in range(m):
        p, e = map(int, input().split())
        primecnt[p, e] += 1
        LCM[p] = max(LCM[p], e)
        tmp.append([p, e])
    A.append(tmp)

ans = 0
nonchange = False
for i in range(n):
    for arr in A[i]:
        p, e = arr
        if LCM[p] != e:
            continue
        if primecnt[p, e] == 1:
            ans += 1
            break
    else:
        nonchange = True

print(ans+nonchange)
