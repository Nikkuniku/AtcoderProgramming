import heapq
from random import randint

a = []
k = 5
for i in range(5):
    a.append(randint(0, 5))
n = sum(a)
m = randint(5, 20)
ans = 10**18
re = []
for c in range(m+1):
    for d in range(m+1):
        for e in range(m+1):
            for f in range(m+1):
                for g in range(m+1):
                    b = []
                    tmp = 0
                    b.append(c)
                    b.append(d)
                    b.append(e)
                    b.append(f)
                    b.append(g)
                    if sum(b) == m and len(b) == k:
                        tmp = 0
                        for i in range(k):
                            tmp = max(abs((b[i]*n)-(a[i]*m)), tmp)

                        if tmp/(n*m) < ans:
                            re = b
                            ans = tmp/(n*m)


def solve(k, n, m, a):
    r = n*m + 2
    l = -1

    def ceil(a, b):
        return -1 * (-a // b)

    while r-l > 1:
        mid = (r+l)//2
        tmp = 0
        for i in range(k):
            tmp += (m*a[i]+mid)//n

        if tmp >= m:
            r = mid
        else:
            l = mid
    b = []
    hanni = []
    for i in range(k):
        p = max(0, ceil(m*a[i]-r, n))
        q = (m*a[i]+r)//n
        hanni.append((p, q))
        b.append(q)

    cnt = sum(b)

    for i in range(k):
        if cnt > m:
            p, q = hanni[i]
            r = cnt-m
            if b[i]-r >= p:
                b[i] -= r
                cnt -= r
            else:
                cnt -= b[i]-p
                b[i] = p
    c = []
    heapq.heapify(c)
    for i in range(k):
        if b[i] > 0:
            c.append([abs(a[i]*m - b[i]*n), i])
    while cnt > m:
        v = heapq.heappop(c)
        p, i = v[0], v[1]
        p += n
        b[i] -= 1
        cnt -= 1
        if b[i] > 0:
            heapq.heappush(c, [p, i])
    print(*b)


print('愚直解')
print(*re)
print('--')
print(k, n, m)
print(*a)
solve(k, n, m, a)
