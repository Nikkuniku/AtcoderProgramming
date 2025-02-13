from collections import defaultdict

N = int(input())
S = input()
d = defaultdict(lambda: -1)
for i, v in enumerate(S):
    d[v] = i
P = sorted(d.items(), key=lambda x: x[1])
ans = [c[0] for c in P]
print(*ans, sep="")
