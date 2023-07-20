from itertools import groupby
N = int(input())
S = input()
gr = groupby(S)
res = 0
for k, v in gr:
    res += 1
ans = 'Yes'
if res != N:
    ans = 'No'
print(ans)
