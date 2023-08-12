N, M, D = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(N)]
picture.sort()
l = -1
r = 1 << 30
while r-l > 1:
    mid = (l+r)//2
    cnt = 0
    pre = -(1 << 30)
    for x, v in picture:
        if pre+D <= x and v >= mid:
            cnt += 1
            pre = x
    if cnt >= M:
        l = mid
    else:
        r = mid
print(l)
