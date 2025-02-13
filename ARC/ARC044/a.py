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


N = int(input())
ans = "Not Prime"
if N == 1:
    exit(print(ans))
primes = make_divisors(N)
if len(primes) == 2:
    ans = "Prime"
elif N % 10 in [1, 3, 7, 9] and sum(map(int, list(str(N)))) % 3 != 0:
    ans = "Prime"

print(ans)
