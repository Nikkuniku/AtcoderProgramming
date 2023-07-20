from math import gcd
A, B = map(int, input().split())
p = abs(A-B)
if p == 0:
    print(1)
    exit()


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


ans = 0
if A > B:
    A, B = B, A
while A > 0 and B > 0:
    g = gcd(A, B)
    if g > 1:
        A, B = A//g, B//g
    t = A
    divisors = make_divisors(B-A)
    for p in divisors:
        if p == 1:
            continue
        t = min(t, A % p)
    A, B = A-t, B-t
    ans += t
print(ans)
