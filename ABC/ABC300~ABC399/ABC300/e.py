from functools import lru_cache


def modinv(a: int, m: int) -> int:
    '''
    モジュラ逆元
    ax mod m =1の解x=a^(-1)を返す

    Parameters
    ----------
    a:int
    m:int
    '''
    x, y, u, v = 1, 0, 0, 1
    M = m
    while m > 0:
        k = a//m
        x -= k*u
        y -= k*v
        x, u = u, x
        y, v = v, y
        a, m = m, a % m
    assert a == 1, "a and m aren't relatively prime numbers"
    if x < 0:
        x += M
    return x


N = int(input())
MOD = 998244353
P = modinv(5, MOD)


@lru_cache(maxsize=None)
def f(n):
    if n >= N:
        return 1 if n == N else 0
    res = 0
    for i in range(2, 7):
        res += f(i*n)
    return res*P % MOD


ans = f(1)
print(ans)
