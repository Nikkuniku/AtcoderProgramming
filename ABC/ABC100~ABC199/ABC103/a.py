A = list(map(int, input().split()))
from itertools import permutations

P = permutations(A)
ans = 1 << 60
for p in P:
    ans = min(ans, abs(p[2] - p[1]) + abs(p[1] - p[0]))
print(ans)
