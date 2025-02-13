from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
A.sort()
ans = 0
for a in A:
    idx = bisect_left(A, 2 * a)
    ans += N - idx
print(ans)
