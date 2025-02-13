N = int(input())
A = list(map(int, input().split()))
maxA = max(A)
l = 0
r = maxA + 1
while r - l > 1:
    mid = (l + r) // 2
    x = maxA ^ mid
    if x <= mid:
        r = mid
    else:
        l = mid
print(r)
