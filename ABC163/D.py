import math
import itertools

N,K=map(int,input().split())

Larges = list(itertools.product([0,1],repeat=N+1))
ans=0
for i in Larges:
    if sum(i)>=K:
        ans+=1

print(ans)