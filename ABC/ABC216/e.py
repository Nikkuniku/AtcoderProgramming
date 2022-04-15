n,k=map(int,input().split())
a=list(map(int,input().split()))

r=10**18
l=-1

while r-l>1:
    mid = (l+r)//2

    cnt=0
    for i in range(n):
        if a[i]>mid:
            cnt+=a[i]-mid
    
    if cnt>k:
        l=mid
    else:
        r=mid
def range_sum(a,b):
    p=a*(a-1)//2
    q=b*(b+1)//2

    return q-p
ans=0
for i in range(n):
    if a[i]-r<0:
        a[i]*=-1
        continue
    else:
        ans+=range_sum(r+1,a[i])
        k-=a[i]-r
        a[i]=r
        a[i]*=-1

import heapq
heapq.heapify(a)
while k>0:
    v=heapq.heappop(a)*(-1)
    if v<=0:
        break
    else:
        ans+=v
        heapq.heappush(a,-(v-1))
        k-=1
print(ans)
