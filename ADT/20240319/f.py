from collections import defaultdict

N, Q = map(int, input().split())
d = defaultdict(set)
ans = []
for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        d[a].add(b)
    elif t == 2:
        d[a].discard(b)
    elif t == 3:
        res = "No"
        if b in d[a] and a in d[b]:
            res = "Yes"
        ans.append(res)
print(*ans, sep="\n")
