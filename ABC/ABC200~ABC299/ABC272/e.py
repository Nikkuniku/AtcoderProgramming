n, m = map(int, input().split())
a = list(map(int, input().split()))
l = 0
r = m+2
while r-l > 1:
    mid = (l+r)//2
    neg_cnt = 0
    for i in range(n):
        if a[i]+(i+1)*mid > 0:
            continue
        neg_cnt += 1

    if neg_cnt > 0:
        l = mid
    else:
        r = mid
print(l, r)
