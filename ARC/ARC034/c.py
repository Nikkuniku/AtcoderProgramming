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


A, B = map(int, input().split())
from collections import defaultdict

d = defaultdict(int)
for k in range(B + 1, A + 1):
    primes = factorization(k)
    for k, e in primes:
        d[k] += e
ans = 1
MOD = 1000000007
for v in d.values():
    ans *= v + 1
    ans %= MOD
print(ans)
