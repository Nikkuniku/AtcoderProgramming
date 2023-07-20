
from math import gcd


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


A, B, K = map(int, input().split())
g = gcd(A, B)
p = make_divisors(g)
p.sort(reverse=True)
ans = p[K-1]
print(ans)
