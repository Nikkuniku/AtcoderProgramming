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


a, m = map(int, input().split())
print(modinv(a, m))
