from collections import defaultdict
N = int(input())
A = [int(input()) for _ in range(N)]
d = defaultdict(int)
for i in range(N-1, -1, -1):
    d[A[i]] = max(d[A[i]], i)
ans = [-1]*N
j = d[A[0]]
c = A[0]
for i in range(N):
    if i <= j:
        ans[i] = c
    else:
        j = d[A[i]]
        c = A[i]
        ans[i] = c
print(*ans, sep="\n")
