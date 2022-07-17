from collections import Counter
n = int(input())
a = list(map(int, input().split()))
a.sort()
c = Counter(a)


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

for p in list(c.keys()):
    m = make_divisors(p)
    for q in m:
        ans += c[p]*c[q]*c[p//q]

print(ans)
