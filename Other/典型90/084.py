n=int(input())
s=list(input())

from itertools import groupby
g=groupby(s)
ans=n*(n-1)//2

for k,v in g:
    v_len=len(list(v))
    if v_len>1:
        ans-=v_len*(v_len-1)//2

print(ans)