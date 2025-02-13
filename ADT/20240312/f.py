from itertools import accumulate

N, M = map(int, input().split())
A = list(map(int, input().split()))
cum = list(accumulate(A, initial=0))
res = sum([(i + 1) * A[i] for i in range(M)])
ans = [res]
for i in range(M, N):
    tmp = cum[i] - cum[i - M]
    res -= tmp
    res += M * A[i]
    ans.append(res)
print(max(ans))
