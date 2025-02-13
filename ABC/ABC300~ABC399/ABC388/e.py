N = int(input())
A = list(map(int, input().split()))
A.sort()
l = 0
r = (N // 2) + 1
while r - l > 1:
    mid = (l + r) // 2
    isOK = True
    for k in range(mid - 1, -1, -1):
        i = N + k - mid
        a, b = A[k], A[i]
        if 2 * a > b:
            isOK = False
    if isOK:
        l = mid
    else:
        r = mid
print(l)
