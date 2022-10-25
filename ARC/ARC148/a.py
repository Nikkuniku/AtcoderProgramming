n = int(input())
a = list(map(int, input().split()))
a.sort()
p = a[-1]-a[0]


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


divisor = make_divisors(p)
ans = 2
for m in [2]+divisor:
    if m == 1:
        continue
    tmp = set()
    for i in range(n):
        tmp.add(a[i] % m)
    ans = min(ans, len(tmp))
print(ans)
