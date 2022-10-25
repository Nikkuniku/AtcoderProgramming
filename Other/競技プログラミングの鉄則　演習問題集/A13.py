from bisect import bisect_right
n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n):
    q = a[i]
    idx = bisect_right(a, q+k)
    ans += idx-(i+1)
print(ans)
