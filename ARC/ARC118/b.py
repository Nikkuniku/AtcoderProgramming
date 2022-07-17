import heapq


k, n, m = map(int, input().split())
a = list(map(int, input().split()))

r = n*m + 2
l = -1


def ceil(a, b):
    return -1 * (-a // b)


while r-l > 1:
    mid = (r+l)//2
    L = 0
    R = 0
    for i in range(k):
        L += max(0, ceil(m*a[i]-mid, n))
        R += (m*a[i]+mid)//n

    if L <= m <= R:
        r = mid
    else:
        l = mid
b = []
hanni = []
for i in range(k):
    p = max(0, ceil(m*a[i]-r, n))
    q = (m*a[i]+r)//n
    hanni.append((p, q))
    b.append(p)

cnt = sum(b)
for i in range(k):
    if cnt < m:
        p, q = hanni[i]
        r = m-cnt
        if b[i]+r > q:
            cnt += q-b[i]
            b[i] = q
        else:
            cnt += r
            b[i] += r
print(*b)
