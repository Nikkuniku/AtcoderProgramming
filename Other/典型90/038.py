a,b=map(int,input().split())
import math

lcm = a*b//math.gcd(a,b)

ans=lcm
if lcm>1000000000000000000:
    ans='Large'


print(ans)