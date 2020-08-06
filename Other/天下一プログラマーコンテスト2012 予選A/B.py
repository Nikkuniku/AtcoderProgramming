

s=list(input())
from itertools import groupby
gr=groupby(s)
ans=[]
for k,v in gr:
    if k==' ':
        ans.append(',')
    else:
        ans.append(k*len(list(v)))

p = ''.join(ans)
print(p)