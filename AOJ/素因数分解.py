def factorization(n: int) -> list:
    '''
    2以上の整数n => [[素因数, 指数], ...]の2次元リスト

    Parameters
    ----------
    n:int
    '''
    arr = []
    temp = n
    for i in range(2, n):
        if i**2 > n:
            break
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
primes = factorization(N)
ans = []
for p, c in primes:
    ans += [p]*c
print('{}:'.format(N), *ans)
