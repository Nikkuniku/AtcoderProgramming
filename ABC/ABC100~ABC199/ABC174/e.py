n, k = map(int, input().split())
a = list(map(int, input().split()))
l = 0
r = max(a)


while r-l > 1:
    mid = (l+r)//2

    tmp = 0
    for i in range(n):
        if a[i] % mid == 0:
            tmp += (a[i]//mid)-1
        else:
            tmp += a[i]//mid

    if tmp <= k:
        r = mid
    else:
        l = mid
print(r)
