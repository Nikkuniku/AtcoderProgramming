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
val = [0] * (N + 1)
for i in range(1, N + 1):
    val[i] = len(make_divisors(i))
ans = 0
for ab in range(1, N + 1):
    ans += val[ab] * val[N - ab]
print(ans)
