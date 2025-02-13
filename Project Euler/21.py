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


N = 10000
S = set()
for a in range(1, N + 1):
    d_a = b = sum(make_divisors(a)) - a
    d_b = sum(make_divisors(b)) - b
    if d_b == a and a != b:
        S.add(a)
        S.add(d_a)
print(sum(S))
