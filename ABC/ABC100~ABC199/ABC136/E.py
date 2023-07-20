from itertools import accumulate


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


N, K = map(int, input().split())
A = list(map(int, input().split()))
S = sum(A)
primes = make_divisors(S)


def solve(d):
    B = [A[i] % d for i in range(N)]
    B.sort()
    ac_L = list(accumulate([0]+B))
    ac_R = [0]
    for i in range(N-1, -1, -1):
        ac_R.append(ac_R[-1]+d-B[i])
    ac_R = ac_R[::-1]
    for i in range(1, N):
        if ac_L[i] == ac_R[i] and ac_L[i] <= K:
            return d
    return 1


ans = 1
for d in primes:
    ans = max(ans, solve(d))
print(ans)
