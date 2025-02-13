N = int(input())
line = [list(map(int, input().split())) for _ in range(N)]
M = sum([a for a, _ in line])


def check_left(k):
    res = 0
    for a, b in line:
        if b * k >= a:
            res += a
            k -= a / b
        else:
            res += b * k
            k = 0
    return res


def check_right(k):
    res = 0
    for a, b in line[::-1]:
        if b * k >= a:
            res += a
            k -= a / b
        else:
            res += b * k
            k = 0
    return res


l = 0
r = 1 << 30
for _ in range(200):
    mid = (l + r) / 2
    L = check_left(mid)
    R = check_right(mid)
    if L + R >= M:
        r = mid
    else:
        l = mid
print(check_left(r))
