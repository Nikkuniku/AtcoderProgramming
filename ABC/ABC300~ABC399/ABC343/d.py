N, T = map(int, input().split())
from collections import defaultdict

d = defaultdict(int)
score = [0] * N
s = set([0])
d[0] = N
ans = []
for _ in range(T):
    a, b = map(int, input().split())
    a -= 1
    pre = score[a]
    d[pre] -= 1
    if d[pre] == 0:
        s.discard(pre)
    new = score[a] + b
    d[new] += 1
    score[a] = new
    s.add(new)
    ans.append(len(s))
print(*ans, sep="\n")
