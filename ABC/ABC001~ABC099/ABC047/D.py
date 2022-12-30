from collections import defaultdict
N, T = map(int, input().split())
A = list(map(int, input().split()))
dp = A[0]
d = defaultdict(int)
for i in range(1, N):
    if dp <= A[i]:
        d[A[i]-dp] += 1
    else:
        dp = A[i]
ans = d[max(d.keys())]
print(ans)
