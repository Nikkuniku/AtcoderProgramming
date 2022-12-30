n,q=map(int,input().split())
a=list(map(int,input().split()))

from collections import defaultdict
d=defaultdict(lambda :-1)
cnt=defaultdict(lambda:0)
for i in range(n):
    cnt[a[i]]+=1
    d[(a[i],cnt[a[i]])]=i+1

ans=[]
for j in range(q):
    x,k=map(int,input().split())
    ans.append(d[(x,k)])
print(*ans,sep="\n")