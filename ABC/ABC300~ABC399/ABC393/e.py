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

N, K = map(int, input().split())
A = list(map(int, input().split()))
dp = defaultdict(int)
for a in A:
    divisors = make_divisors(a)
    for d in divisors:
        if d == 1:
            continue
        dp[d] += 1
ans = []
for a in A:
    divisors = make_divisors(a)
    res = 1
    for d in divisors:
        if d == 1:
            continue
        if dp[d] >= K:
            res = max(res, d)
    ans.append(res)
print(*ans, sep="\n")
