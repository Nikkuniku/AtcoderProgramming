from collections import defaultdict
N, M, T = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(lambda: 0)
for _ in range(M):
    x, y = map(int, input().split())
    d[x] = y
ans = 'Yes'
for i in range(N-1):
    if T-A[i] > 0:
        T -= A[i]
        T += d[i+2]
    else:
        ans = 'No'
print(ans)
