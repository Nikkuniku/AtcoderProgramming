n,k=map(int,input().split())
a=list(map(int,input().split()))
from collections import defaultdict,deque
import bisect
def solve():
    pre=0
    ind=[]
    d=defaultdict(int)
    for j in range(k,n):
        if pre<a[j]:
            ind.append(a[j])
            d[a[j]]=j
            pre=a[j]
    tmp=10**18
    for i in range(k):
        q=bisect.bisect_right(ind,a[i])
        if q==len(ind):continue
        j=d[ind[q]]
        tmp=min(j-i,tmp)

    ans=-1
    if tmp!=10**18:
        ans=tmp
    print(ans)
solve()