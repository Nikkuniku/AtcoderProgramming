from itertools import accumulate

N, M = map(int, input().split())
ans = [0] * (N + 3)


def add_line(l, r, a, d):
    ans[l] += a
    ans[l + 1] += d - a
    ans[r] += -(d * (r - l)) - a
    ans[r + 1] += d * (r - l - 1) + a


for _ in range(M):
    p, q = map(int, input().split())
    if p - (q - 1) >= 1:
        add_line(p + 1 - q, p + 1, 1, 1)
    else:
        add_line(1, p + 1, q - (p - 1), 1)
    if p + (q - 1) <= N:
        add_line(p + 1, p + q, q - 1, -1)
    else:
        add_line(p + 1, N + 1, q - 1, -1)

ans = list(accumulate(list(accumulate(ans))))
print(*ans[1 : (N + 1)])
