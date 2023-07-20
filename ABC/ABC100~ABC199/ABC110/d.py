def factorization(n: int) -> list:
    '''
    2以上の整数n => [[素因数, 指数], ...]の2次元リスト

    Parameters
    ----------
    n:int
    '''
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
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


k = 2 * 10**5 + 5
mod = 10**9 + 7

fact = [1]*k  # fact[n] = (n! mod p)
factinv = [1]*k  # factinv[n] = ((n!)^(-1) mod p)
inv = [0]*k  # factinv 計算用
inv[1] = 1
for i in range(2, k):
    fact[i] = (fact[i-1]*i) % mod
    inv[i] = (mod - inv[mod % i]*(mod//i)) % mod
    factinv[i] = factinv[i-1]*inv[i] % mod


def cmb(n, r, p):
    re = 1
    for j in range(r):
        re = re*(n-j) % p
    re = re*factinv[r] % p
    return re


N, M = map(int, input().split())
primes = factorization(M)
ans = 1
for p, e in primes:
    if p == 1:
        continue
    ans *= cmb(N-1+e, e, mod)
    ans %= mod
print(ans)
