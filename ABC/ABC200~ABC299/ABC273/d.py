from collections import defaultdict
from bisect import bisect_left
H, W, rs, cs = map(int, input().split())
row = defaultdict(lambda: [0, W+1])
col = defaultdict(lambda: [0, H+1])

N = int(input())
for _ in range(N):
    r, c = map(int, input().split())
    row[r].append(c)
    col[c].append(r)

for p in row.keys():
    row[p] = sorted(row[p])
for p in col.keys():
    col[p] = sorted(col[p])

q = int(input())
ans = []
for _ in range(q):
    d, l = input().split()
    l = int(l)
    if d == 'L':
        idx = bisect_left(row[rs], cs)
        a = row[rs][idx-1]
        cs = max(a+1, cs-l)
    elif d == 'U':
        idx = bisect_left(col[cs], rs)
        a = col[cs][idx-1]
        rs = max(a+1, rs-l)
    elif d == 'R':
        idx = bisect_left(row[rs], cs)
        a = row[rs][idx]
        cs = min(a-1, cs+l)
    elif d == 'D':
        idx = bisect_left(col[cs], rs)
        a = col[cs][idx]
        rs = min(a-1, rs+l)
    ans.append([rs, cs])
for c in ans:
    print(*c)
