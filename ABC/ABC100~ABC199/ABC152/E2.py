from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
MOD = 10**9 + 7


def inv(b):
    return pow(b, MOD-2, MOD)


"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""


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


for a in A:
    primes = factorization(a)
    for p, c in primes:
        d[p] = max(d[p], c)

L = 1
for k, v in d.items():
    L *= pow(k, v, MOD)
    L %= MOD
ans = 0
for a in A:
    ans += L*inv(a)
    ans %= MOD
print(ans)
