N = int(input())


def poly(a, b, c, x):
    return a * x * x + b * x + c


def solve(d, n):
    l = 0
    r = 1 << 60
    while r - l > 1:
        mid = (l + r) // 2
        if poly(3, 3 * d, d * d - n, mid) <= 0:
            l = mid
        else:
            r = mid
    if poly(3, 3 * d, d * d - n, l) == 0:
        return True, l
    return False, -1


for d in range(1, N):
    if d * d * d > N:
        break
    if N % d != 0:
        continue
    M = N // d
    isOK, y = solve(d, M)
    if isOK:
        exit(print(y + d, y))
print(-1)
