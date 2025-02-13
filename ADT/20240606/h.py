from random import randint
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = sorted(set(A + B))
d = defaultdict(int)
for c in C:
    r = randint(1, 1 << 40)
    d[c] = r
Q = int(input())
cuma = [0]
cumb = [0]
sa = set()
sb = set()
for a in A:
    a = d[a]
    if a not in sa:
        tmp = cuma[-1] ^ a
    else:
        tmp = cuma[-1]
    cuma.append(tmp)
    sa.add(a)
for b in B:
    b = d[b]
    if b not in sb:
        tmp = cumb[-1] ^ b
    else:
        tmp = cumb[-1]
    cumb.append(tmp)
    sb.add(b)
ans = []
for _ in range(Q):
    x, y = map(int, input().split())
    res = "No"
    if cuma[x] == cumb[y]:
        res = "Yes"
    ans.append(res)
print(*ans, sep="\n")
