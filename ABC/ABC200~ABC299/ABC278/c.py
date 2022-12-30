from collections import defaultdict
N, Q = map(int, input().split())
d = defaultdict(int)
ans = []
for _ in range(Q):
    T, a, b = map(int, input().split())
    if T == 1:
        d[(a, b)] = 1
    elif T == 2:
        d[(a, b)] = 0
    else:
        if d[(a, b)] and d[(b, a)]:
            ans.append('Yes')
        else:
            ans.append('No')

print(*ans, sep="\n")
