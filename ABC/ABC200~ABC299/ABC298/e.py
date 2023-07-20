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


N, A, B, P, Q = map(int, input().split())
dp_t = [0]*(N+1)
dp_a = [0]*(N+1)
dp_t[A] = 1
dp_a[B] = 1
MOD = 998244353
bunsi = 0
bunbo = 0
for _ in range(100):
    for i in range(N-1, A-1, -1):
        for j in range(1, P+1):
            dp_t[min(i+j, N)] += dp_t[i]
        dp_t[i] = 0
    bunsi += dp_t[N]*sum(dp_a[:N])
    bunbo += dp_t[N]*sum(dp_a[:N])
    bunsi %= MOD
    bunbo %= MOD
    dp_t[N] = 0

    for i in range(N-1, B-1, -1):
        for j in range(1, Q+1):
            dp_a[min(i+j, N)] += dp_a[i]
        dp_a[i] = 0
    if dp_a[N] > 0:
        bunbo += sum(dp_t[:N])
ans = bunsi*modinv(bunbo, MOD) % MOD
print(ans)
