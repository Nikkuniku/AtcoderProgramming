from collections import defaultdict

N = int(input())
P = list(map(int, input().split()))
d = defaultdict(int)
for i, v in enumerate(P):
    d[v] = i

Q = int(input())
ans = []
for _ in range(Q):
    a, b = map(int, input().split())
    if d[a] < d[b]:
        ans.append(a)
    else:
        ans.append(b)
print(*ans, sep="\n")
