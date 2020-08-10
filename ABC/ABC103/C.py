n=int(input())
a=list(map(int,input().split()))


import math

ans = a[0]
for i in range(1, n):
    ans = ans * a[i] // math.gcd(ans, a[i])



s = 0

for i in range(n):
    s += (ans-1)%a[i]

print(s)