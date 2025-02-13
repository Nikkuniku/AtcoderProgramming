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


N = int(input())
A = list(map(int, input().split()))
from collections import defaultdict

d = defaultdict(list)
for a in A:
    if a == 0:
        d[a].append(a)
        continue
    primes = factorization(a)
    tmp = 1
    for p, e in primes:
        tmp *= 1 if e % 2 == 0 else p
    d[tmp].append(a)
ans = 0
for k, v in d.items():
    m = len(v)
    if k == 0:
        ans += m * (N - m)
    ans += m * (m - 1) // 2
print(ans)
