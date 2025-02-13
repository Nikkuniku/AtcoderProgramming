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
M = list(map(int, input().split()))
xor = 0
for m in M:
    primes = factorization(m)
    x = 0
    for _, e in primes:
        x ^= e % 3
    xor ^= x
ans = "Alice" if xor else "Bob"
print(ans)
