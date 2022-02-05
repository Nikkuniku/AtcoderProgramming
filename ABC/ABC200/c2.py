n=int(input())
a=list(map(int,input().split()))

from collections import defaultdict
d=defaultdict(int)

for i in range(n):
    p=a[i]%200
    d[p]+=1

ans=0
for p in d.keys():
    for q in d.keys():
        if (p-q)%200==0:
            if p==q:
                ans+=d[p]*(d[p]-1)//2
            else:
                ans+=d[p]*d[q]

print(ans)