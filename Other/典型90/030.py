import sys

# limit 以下の全ての素数を返す
def list_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range (0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p*p, limit + 1, p):
            is_prime[i] = False

    return primes
n,k=map(int,input().split())
p=list_primes(n)
primes=[0]*(n+1)

for i in p:
    j=i
    while j<n+1:
        primes[j]+=1
        j+=i
ans=0

for l in range(len(primes)):
    if primes[l]>=k:
        ans+=1
print(ans)