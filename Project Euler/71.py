from math import gcd

ans = 0
numerator = -1
denominator = -1
N = 1000000
for d in range(2, N + 1):
    for n in range(3 * d // 7, 0, -1):
        if gcd(n, d) == 1:
            if d * ans < n and 7 * n < 3 * d:
                ans = n / d
                numerator = n
                denominator = d
            break
print(ans, numerator, denominator)
