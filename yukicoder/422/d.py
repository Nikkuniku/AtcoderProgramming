def gcd(a, b):
    while a:
        a, b = b % a, a
    return b


def is_prime(n):
    if n == 2:
        return 1
    if n == 1 or n % 2 == 0:
        return 0

    m = n - 1
    lsb = m & -m
    s = lsb.bit_length() - 1
    d = m // lsb

    test_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in test_numbers:
        if a == n:
            continue
        x = pow(a, d, n)
        r = 0
        if x == 1:
            continue
        while x != m:
            x = pow(x, 2, n)
            r += 1
            if x == 1 or r == s:
                return 0
    return 1


def find_prime_factor(n):
    if n % 2 == 0:
        return 2

    m = int(n**0.125) + 1

    for c in range(1, n):
        f = lambda a: (pow(a, 2, n) + c) % n
        y = 0
        g = q = r = 1
        k = 0
        while g == 1:
            x = y
            while k < 3 * r // 4:
                y = f(y)
                k += 1
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            k = r
            r *= 2
        if g == n:
            g = 1
            y = ys
            while g == 1:
                y = f(y)
                g = gcd(abs(x - y), n)
        if g == n:
            continue
        if is_prime(g):
            return g
        elif is_prime(n // g):
            return n // g
        else:
            return find_prime_factor(g)


def factorize(n):
    res = {}
    while not is_prime(n) and n > 1:  # nが合成数である間nの素因数の探索を繰り返す
        p = find_prime_factor(n)
        s = 0
        while n % p == 0:  # nが素因数pで割れる間割り続け、出力に追加
            n //= p
            s += 1
        res[p] = s
    if n > 1:  # n>1であればnは素数なので出力に追加
        res[n] = 1
    return res


N, K = map(int, input().split())
A = list(map(int, input().split()))
from collections import defaultdict

d = defaultdict(bool)
P = factorize(K)
S = set()
for k, v in P.items():
    d[pow(k, v)] = False
    S.add(pow(k, v))
for a in A:
    for s in S:
        if a % s == 0:
            d[s] = True
            S.discard(s)
            break

ans = "Yes" if len(S) == 0 else "No"
print(ans)
