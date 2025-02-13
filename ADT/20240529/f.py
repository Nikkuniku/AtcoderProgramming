from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(list)
for i, a in enumerate(A):
    d[a].append(i + 1)
ans = []
for _ in range(Q):
    x, k = map(int, input().split())
    if len(d[x]) < k:
        ans.append(-1)
    else:
        ans.append(d[x][k - 1])
print(*ans, sep="\n")
