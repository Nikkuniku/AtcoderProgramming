def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N = 1000000
p = 0
s = 1
for n in range(2, 15000):
    a = 4 * (n**2) - 10 * n + 7
    b = 4 * (n**2) - 8 * n + 5
    c = 4 * (n**2) - 6 * n + 3
    d = 4 * (n**2) - 4 * n + 1
    if len(make_divisors(a)) == 2:
        p += 1
    if len(make_divisors(b)) == 2:
        p += 1
    if len(make_divisors(c)) == 2:
        p += 1
    if len(make_divisors(d)) == 2:
        p += 1
    s += 4
    if 10 * p < s:
        print(n, 3 + (n - 2) * 2)
        break
