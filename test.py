# # import sys
# # print(sys.version_info)

import numpy as np 
A=np.array([1,2,3])
print(A+A)


import math 

print(math.gcd(589,403))

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

print(primes(100000))
print(len(primes(100000)))