from bisect import bisect_left, bisect_right
n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
cumsum = [0]
for i in range(n):
    cumsum.append(cumsum[-1]+a[i])


ans = []
for _ in range(q):
    x = int(input())
    r = bisect_right(a, x)
    p = cumsum[n]-cumsum[r] - x*(n-r)

    l = bisect_left(a, x)
    q = x*l-cumsum[l]

    re = p+q
    ans.append(re)
print(*ans, sep="\n")
