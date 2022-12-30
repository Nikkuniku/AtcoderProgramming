"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""




from math import log, floor
from collections import defaultdict
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


K = int(input())
primes = factorization(K)
if len(primes) == 1:
    ans = primes[0][0]
    print(ans)
else:
    ans = []
    d = defaultdict(int)
    s = set()
    for p, c in primes:
        d[p] = c
        s.add(p)
    for x in range(10000000):
        primes_x = factorization(x)
        for p, c in primes_x:
            d[p] -= c
            if d[p] <= 0:
                s.discard(p)

        if not s:
            break
    print(x)
