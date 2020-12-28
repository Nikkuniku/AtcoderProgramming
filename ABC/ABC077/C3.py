n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

a=sorted(a)
c=sorted(c)

import bisect

ans=0
for b_i in b:

    j=bisect.bisect_left(a,b_i)

    k=bisect.bisect_right(c,b_i)

    ans+=j*(n-k)

print(ans)