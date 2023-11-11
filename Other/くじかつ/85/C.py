n=int(input())
d=list(map(int,input().split()))

m=int(input())
t=list(map(int,input().split()))

from collections import Counter

c =dict(Counter(d)) 

ans='YES'
for i in range(m):
    p = t[i]

    if p in c:
        if c[p]>=1:
            c[p]-=1
        else:
            ans='NO'
            break
    else:
        ans='NO'
        break

print(ans)

