import random


def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n & 1 == 0:
        return False

    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1

    for k in range(100):
        a = random.randint(1, n - 1)
        t = d
        y = pow(a, t, n)

        while t != n - 1 and y != 1 and y != n - 1:
            y = (y * y) % n
            t <<= 1

        if y != n - 1 and t & 1 == 0:
            return False

    return True


def t(n):
    return 2 * n * n - 1


N = 50000000
ans = 0
for n in range(1, N + 1):
    if is_prime(t(n)):
        ans += 1
print(ans)
