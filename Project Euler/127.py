def factorization(n: int) -> list:
    """
    2以上の整数n => [[素因数, 指数], ...]の2次元リスト

    Parameters
    ----------
    n:int
    """
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append((i, cnt))

    if temp != 1:
        arr.append((temp, 1))

    if arr == []:
        arr.append((n, 1))

    return arr


from math import gcd

N = 120000
rad = [1] * (N + 1)
for n in range(1, N + 1):
    factors = factorization(n)
    for p, _ in factors:
        rad[n] *= p
ans = 0
for c in range(1, N):
    for a in range(1, c // 2):
        b = c - a
        if a >= b:
            break
        if gcd(a, b) == gcd(b, c) == gcd(a, c) == 1:
            if rad[a] * rad[b] * rad[c] < c:
                ans += c
print(ans)
