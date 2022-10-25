n, k = map(int, input().split())
a = list(map(int, input().split()))

l = 0
r = 10**9 + 2
while r-l > 1:
    mid = (l+r)//2
    tmp = 0
    for i in range(n):
        tmp += mid//a[i]

    if tmp >= k:
        r = mid
    else:
        l = mid

print(r)
