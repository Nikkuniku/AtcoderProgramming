from math import gcd


def modinv(a, b):
    p = b
    x, y, u, v = 1, 0, 0, 1
    while b:
        k = a // b
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    x %= p
    if x < 0:
        x += p
    return x


def solve(N, S, K):
    g = gcd(N, K)
    res = -1
    if S % g != 0:
        return res
    else:
        N //= g
        S //= g
        K //= g
        res = (-S*modinv(K, N)) % N
        return res


T = int(input())
ans = []
for _ in range(T):
    N, S, K = map(int, input().split())
    ans.append(solve(N, S, K))
print(*ans, sep="\n")
