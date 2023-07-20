from itertools import groupby
N = int(input())
S = input()
gr = groupby(S)
ans = -1
a = []
for k, v in gr:
    a.append((k, len(list(v))))
for i in range(len(a)):
    tmp = -1
    if i < len(a)-1:
        if a[i][0] == '-':
            tmp = a[i+1][1]
        else:
            tmp = a[i][1]
    else:
        if len(a) > 1 and a[i][0] == 'o':
            tmp = a[i][1]
    ans = max(ans, tmp)

print(ans)
