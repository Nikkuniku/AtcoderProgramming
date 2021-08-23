n = int(input())
x = list(map(int, input().split()))
# limit 以下の全ての素数を返す
def list_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range(0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p*p, limit + 1, p):
            is_prime[i] = False

    return primes

p = list_primes(max(x))
ans = 10**30
for i in range(1 << len(p)):
    divided = [False]*n
    tmp = 1
    for j in range(len(p)):
        if (i >> j) & 1:
            a = p[j]

            for k in range(n):
                if x[k] % a == 0:
                    divided[k] = True
            tmp *= a
    if all(divided):
        ans = min(ans, tmp)

print(ans)
