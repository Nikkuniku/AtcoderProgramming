n, k = map(int, input().split())
a = list(map(int, input().split()))
l = -1
r = 10**12 + 2
while r-l > 1:
    mid = (l+r)//2
    apple = 0
    for i in range(n):
        apple += min(a[i], mid)

    if apple > k:
        r = mid
    else:
        l = mid

for i in range(n):
    if a[i] >= l:
        k -= l
        a[i] -= l
    else:
        k -= a[i]
        a[i] = 0
for i in range(n):
    if k > 0:
        if a[i] > 0:
            a[i] -= 1
            k -= 1
    else:
        break

print(*a)
