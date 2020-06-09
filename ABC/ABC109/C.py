n,x = map(int,input().split())
city = list(map(int,input().split()))

from fractions import gcd

if n==1:
    print(abs(city[0]-x))
    exit(0)

city = sorted(city)

for i in range(n):
    city[i]-=x

for j in range(n):
    if j==0:
        ans = gcd(city[j],city[j+1])
    else:
        ans = gcd(ans,city[j])

print(abs(ans))