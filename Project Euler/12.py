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


for i in range(100, 554400):
    a = ((i + 1) * i) // 2
    primes = make_divisors(a)
    if len(primes) >= 500:
        print(i)
        print(a)
        print(len(primes))
        break
