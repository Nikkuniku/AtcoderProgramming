from itertools import combinations

N, K = map(int, input().split())
A = list(map(int, input().split()))
S = 0
for a in A:
    S ^= a
L = N - K
ans = -1
if K >= N - K:
    C = list(combinations(range(N), N - K))
    for c in C:
        temp = 0
        for p in c:
            temp ^= A[p]
        ans = max(ans, S ^ temp)
else:
    C = list(combinations(range(N), K))
    ans = -1
    for c in C:
        temp = 0
        for p in c:
            temp ^= A[p]
        ans = max(ans, temp)
print(ans)
