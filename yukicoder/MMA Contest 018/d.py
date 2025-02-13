N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
from collections import defaultdict
from bisect import bisect_right

five = defaultdict(list)
seven = defaultdict(int)
nine = defaultdict(int)
ten = defaultdict(int)
for a in A:
    seven[a] = pow(7, a, P)
    nine[a] = pow(9, a, P)
    ten[a] = pow(10, a, P)
    five[pow(5, a, P)].append(a)
ans = 0
for a in range(N):
    for b in range(a + 1, N):
        for c in range(b + 1, N):
            x = (ten[A[a]] + nine[A[b]] + seven[A[c]]) % P
            y = len(five[(Q - x) % P]) - bisect_right(five[(Q - x) % P], A[c])
            ans += y
print(ans)
