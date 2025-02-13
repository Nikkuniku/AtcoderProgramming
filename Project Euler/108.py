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


# N = 1000000
# for i in range(1, N):
#     D = make_divisors(i * i)
#     if (len(D) + 1) // 2 >= 1000:
#         exit(print(i))

print(len(make_divisors(180180 * 180180)))
