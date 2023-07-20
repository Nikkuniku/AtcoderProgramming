from itertools import groupby
S = input()
gr = groupby(S)
arr = [[], []]
tri = []
for k, v in gr:
    t = len(list(v))
    arr[int(k)].append(t)
    tri.append(t)
ans = 0
can = []
if len(tri) > 2:
    for i in range(len(tri)-1):
        can.append(tri[i]+tri[i+1])
    ans = min(can)
for i in range(2):
    if arr[i]:
        ans = max(ans, min(arr[i]))
print(ans)
