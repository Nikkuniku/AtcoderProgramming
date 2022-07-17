N, a, b = map(int, input().split())
A = list(map(int, input().split()))


def ceil(a, b):
    return -(-a//b)


l = -1
r = 1000000002
while r-l > 1:
    mid = (l+r)//2
    p = 0
    q = 0
    for i in range(N):
        if A[i] < mid:
            p += ceil(mid-A[i], a)
        else:
            q += (A[i]-mid)//b

    if p <= q:
        l = mid
    else:
        r = mid
print(l)
