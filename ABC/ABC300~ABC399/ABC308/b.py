from collections import defaultdict
N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
p0, *P = list(map(int, input().split()))
d = defaultdict(lambda: p0)
for i in range(M):
    d[D[i]] = P[i]
ans = 0
for c in C:
    ans += d[c]
print(ans)
