N, M = map(int, input().split())
A = list(map(int, input().split()))
l = 0
r = 1 << 60
while r - l > 1:
    mid = (l + r) // 2
    tmp = 0
    cnt = 1
    if max(A) > mid:
        l = mid
        continue
    for a in A:
        if tmp + a <= mid:
            tmp += a + 1
        else:
            tmp = a + 1
            cnt += 1
    if cnt > M:
        l = mid
    else:
        r = mid
print(r)
