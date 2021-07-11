def sieve_eratosthenes(n):
    primes = [0, 1] * (n // 2 + 1)
    if n % 2 == 0:
        primes.pop()
    primes[1] = 0
    primes[2] = 1
    for p in range(3, int(n ** 0.5) + 1, 2):
        if primes[p]:
            for q in range(p * p, n + 1, 2 * p):
                primes[q] = 0
    return primes

n=int(input())

p=sieve_eratosthenes(n)

ans=0
for i in range(len(p)):
    if p[i]==1:
        ans+=i

print(ans)