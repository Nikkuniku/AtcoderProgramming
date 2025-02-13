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


MOD = 998244353
K = 2 * 10**5  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, K + 1):
    fact.append((fact[-1] * i) % MOD)
    inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

N, M = map(int, input().split())
ans = 0
for v in range(1, M + 1):
    primes = factorization(v)
    tmp = 1
    for p, e in primes:
        if p == 1:
            continue
        for j in range(e):
            tmp *= N + j
        tmp *= factinv[e]
        tmp %= MOD
    ans += tmp
    ans %= MOD
print(ans)
