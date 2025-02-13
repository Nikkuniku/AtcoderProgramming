def sieve_of_eratosthenes(x):
    nums = [i for i in range(x + 1)]

    root = int(pow(x, 0.5))
    for i in range(2, root + 1):
        if nums[i] != 0:
            for j in range(i, x + 1):
                if i * j >= x + 1:
                    break
                nums[i * j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes


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


def digitlen(n):
    digit = []
    while n > 0:
        digit.append(n % 10)
        n //= 10
    return len(digit)


n = int(input())
primes = sieve_of_eratosthenes(n)
ans = 0
for i in range(len(primes) - 1):
    if not 5 <= primes[i] <= 1000000:
        continue
    p1, p2 = primes[i], primes[i + 1]
    L = digitlen(p1)
    q = (((-p1) % p2) * modinv(pow(10, L, p2), p2)) % p2
    S = pow(10, L) * q + p1
    ans += S
print(ans)
