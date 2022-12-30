a,b,c,d = map(int,input().split())
ans=-1

from math import ceil
if c*d-b>0:
    ans = ceil(a/(c*d-b))

print(ans)
