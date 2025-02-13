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
M = [0] * (N + 1)
for v in range(1, N + 1):
    divisors = make_divisors(v)
    M[v] = len(divisors)
ans = 0
for k in range(1, N):
    ans += M[k] * M[N - k]
print(ans)
