N=int(input())
S=list(input())

from itertools import groupby

slime = groupby(S)

ans=0
for key ,_ in slime:
    ans+=1

print(ans)