from collections import defaultdict
N, Q = map(int, input().split())
d = defaultdict(int)
ans = []
for _ in range(Q):
    q, x = map(int, input().split())
    if q == 1:
        d[x] += 1
    elif q == 2:
        d[x] = 2
    else:
        res = 'No'
        if d[x] == 2:
            res = 'Yes'
        ans.append(res)
print(*ans, sep="\n")
