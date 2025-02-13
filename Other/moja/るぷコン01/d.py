def modinv(a: int, m: int) -> int:
    """
    モジュラ逆元
    ax mod m =1の解x=a^(-1)を返す

    Parameters
    ----------
    a:int
    m:int
    """
    x, y, u, v = 1, 0, 0, 1
    M = m
    while m > 0:
        k = a // m
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, m = m, a % m
    assert a == 1, "a and m aren't relatively prime numbers"
    if x < 0:
        x += M
    return x


N, M, T = map(int, input().split())
adjacent = [[] for _ in range(N)]
for _ in range(M):
    u, v, t = map(int, input().split())
    u -= 1
    v -= 1
    adjacent[u].append((v, t))
    adjacent[v].append((u, t))
dp = [[0] * (T + 1) for _ in range(N)]
dp[0][0] = 1
MOD = 998244353
for t in range(T):
    for v in range(N - 1):
        if not adjacent[v]:
            continue
        P = modinv(len(adjacent[v]), MOD)
        for e, cost in adjacent[v]:
            if t + cost > T:
                continue
            dp[e][t + cost] += dp[v][t] * P
            dp[e][t + cost] %= MOD
ans = 0
for i in range(T + 1):
    ans += dp[N - 1][i]
    ans %= MOD
print(ans)
