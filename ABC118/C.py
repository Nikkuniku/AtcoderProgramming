n = int(input())
a= list(map(int,input().split()))

from fractions import gcd

ans =0
for i in range(n-1):
    if i==0:
        ans = gcd(a[i],a[i+1])
    else:
        ans = gcd(ans,a[i+1])

print(ans)