n=int(input())
from math import sqrt
for k in range(1,n+1):

    ans=0
    p=int(sqrt(k))
    for i in range(3,p+1):

        for x in range(1,i):
            for y in range(1,i-x):
                z=x-y
                if x**2 + y**2 + z**2 +x*y + y*z +z*x==k:
                    ans+=1

    print(ans)