def judge(k, a, b):
    x = (k**2 - b**2)**0.5
    y = (k**2 - a**2)**0.5
    if k <= a:
        y = 0
        a = k
    if k <= b:
        x = 0
        b = k
    res = False
    if (y-b)**2 + (a-x)**2 >= k**2:
        res = True
    return res


A, B = map(int, input().split())
l = min(A, B)
r = 2*max(A, B)
for _ in range(300):
    mid = (l+r)/2
    if judge(mid, A, B):
        l = mid
    else:
        r = mid
print(l)
