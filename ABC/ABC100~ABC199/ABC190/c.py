n,m=map(int,input().split())
con=[tuple(map(int,input().split())) for _ in range(m)]
k=int(input())
ball=[tuple(map(int,input().split())) for _ in range(k)]
ans=0
import itertools

for c in itertools.product(*ball):
    s=set(c)
    tmp=0
    for x in con:
        if x[0] in s and x[1] in s:
            tmp+=1
    ans=max(ans,tmp)

print(ans)