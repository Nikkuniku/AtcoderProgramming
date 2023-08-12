def make_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


N, K = map(int, input().split())
primes = make_divisors(N-K)
ans = 0
for p in primes:
    if N % p == K:
        ans += 1
print(ans)
