n=int(input())

from fractions import gcd
def lcm(a,b):
    return a*b //gcd(a,b)

t=1

for _ in range(n):
    t_i = int(input())

    t = lcm(t,t_i)

print(t)
