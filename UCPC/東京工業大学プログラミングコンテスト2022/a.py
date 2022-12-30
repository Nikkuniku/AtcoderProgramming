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


X, Y = map(int, input().split())
a = make_divisors(X-2015)
b = make_divisors(Y-2015)
ans = sorted(list(set(a) & set(b)))
print(*ans, sep="\n")
