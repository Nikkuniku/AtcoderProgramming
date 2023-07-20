N, A, B = map(int, input().split())
H = [int(input()) for _ in range(N)]


def ceil(a, b):
    return -(-a//b)


def check(k):
    cnt = 0
    for i in range(N):
        cnt += ceil(max(0, H[i]-B*k), A-B)
    if cnt <= k:
        return True
    return False


r = 1 << 60
l = -1
while r-l > 1:
    mid = (l+r)//2
    if check(mid):
        r = mid
    else:
        l = mid
print(r)
