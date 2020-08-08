q=int(input())

import math
import numpy as np
def primes(x):
    if x < 2: return []

    primes = [i for i in range(x)]
    primes[1] = 0 # 1は素数ではない

    # エラトステネスのふるい
    for prime in primes:
        if prime > math.sqrt(x): break
        if prime == 0: continue
        for non_prime in range(2 * prime, x, prime): primes[non_prime] = 0

    return [prime for prime in primes if prime != 0]



numbers=[0]*100000
prime=primes(100_000)

for j in prime:
    numbers[j-1]=1

deci=numbers.copy()

for p in prime:
    n_2 = (p+1)//2

    if deci[n_2-1]==1:
        continue
    else:
        numbers[p-1]=0

cum=np.cumsum(numbers)

for i in range(q):
    l,r=map(int,input().split())

    if l==1:
        ans=cum[r-1]
    else:
        ans=cum[r-1] - cum[l-2]

    print(ans)