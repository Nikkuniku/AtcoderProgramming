n = int(input())

# 存在しない列を見つける
l = 0
r = n+1
mid = (l+r)//2
lq = 1
rq = mid
while r-l > 1:
    print('?', 1, n, lq, rq, flush=True)
    t = int(input())
    if t < rq-lq+1:
        r = mid
        mid = (l+r)//2
        lq = max(1, l)
        rq = mid
    else:
        l = mid
        mid = (l+r)//2
        lq = mid
        rq = min(r, n)
y = r

l = 0
r = n+1
mid = (l+r)//2
lq = 1
rq = mid
while r-l > 1:
    print('?',  lq, rq, 1, n, flush=True)
    t = int(input())
    if t < rq-lq+1:
        r = mid
        mid = (l+r)//2
        lq = max(1, l)
        rq = mid
    else:
        l = mid
        mid = (l+r)//2
        lq = mid
        rq = min(r, n)

x = r
print('!', x, y, flush=True)
