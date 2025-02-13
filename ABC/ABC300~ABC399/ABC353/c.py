from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
ans = 0
L = 10**8
for i in range(N):
    ans += A[i] * (N - 1)
A.sort()
for i in range(N):
    a = A[i]
    idx = bisect_left(A, L - a)
    if idx <= i:
        idx = i + 1
    tmp = (N - idx) * L
    ans -= tmp
print(ans)
