from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
ans = 0
cum = list(accumulate(A, initial=0))
for i in range(N):
    temp = A[i] * (cum[N] - cum[i + 1])
    ans += temp
print(ans)
