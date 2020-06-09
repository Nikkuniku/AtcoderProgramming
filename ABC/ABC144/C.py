N=int(input())

from itertools import combinations
import math

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

d=make_divisors(N)

if math.sqrt(N) in d:
    d.append(int(math.sqrt(N)))

dist=float('inf')
for i in d:
    j = N//i
    if i * j ==N:
        dist = min(dist,i+j-2)

print(dist)
    