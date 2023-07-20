from collections import defaultdict


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


N = int(input())
S = input()
Divisor = make_divisors(N)
A = defaultdict(int)
MOD = 998244353
ans = 0
for t in Divisor:
    if t == N:
        continue
    holidays = defaultdict(int)
    for i in range(N):
        if S[i] == '.':
            holidays[(i+1) % t] = 1
    CNT = t-len(holidays.keys())
    A[t] = pow(2, CNT, MOD)
    for u in make_divisors(t):
        if u < t:
            A[t] -= A[u]
    A[t] %= MOD
    ans += A[t]
    ans %= MOD
print(ans)
