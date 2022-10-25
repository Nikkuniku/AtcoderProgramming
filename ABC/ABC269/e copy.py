n = int(input())


def send(a, b, c, d):
    print('?', a, b, c, d, flush=True)


# 存在しない列を見つける
l = 1
r = n+1
while r-l >= 1:
    mid = (l+r)//2
    send(1, n, l, mid)
    t = int(input())
    if t == mid-l+1:
        l = mid+1
    else:
        r = mid
y = l

l = 1
r = n+1
while r-l >= 1:
    mid = (l+r)//2
    send(l, mid, 1, n)
    t = int(input())
    if t == mid-l+1:
        l = mid+1
    else:
        r = mid
x = l
print('!', x, y, flush=True)
