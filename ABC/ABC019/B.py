s=list(input())
from itertools import groupby

gr = groupby(s)

ans=''
for k,v in gr:
    ans+= k + str(len(list(v)))

print(ans)