a = int(input())
b = int(input())
n = int(input())

from fractions import gcd

lcm = a*b/gcd(a,b)

for i in range(n,n*1000):
    if i%a==0 and i%b==0:
        print(i)
        exit(0)