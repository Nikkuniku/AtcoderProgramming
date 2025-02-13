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


from collections import defaultdict

N = int(input())
Squares = set([i * i for i in range(N + 1)])
d = defaultdict(int)
for i in range(1, N + 1):
    divisors = make_divisors(i)
    res = -1
    for div in divisors:
        if div in Squares:
            res = div
    d[i // res] += 1
ans = 0
for v in d.values():
    ans += v * v
print(ans)
