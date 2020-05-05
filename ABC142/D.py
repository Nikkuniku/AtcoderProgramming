def prime_factor(n):
    ass = []
    for i in range(2,int(n**0.5)+1):
        while n % i==0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass

A,B = map(int,input().split())

A_s = set(prime_factor(A))
B_s = set(prime_factor(B))

from fractions import gcd

print(len(A_s&B_s)+1)
