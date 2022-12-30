n,k=map(int,input().split())
a=list(map(int,input().split()))

from collections import defaultdict

prevSum=defaultdict(lambda:0)
res=0
cursum=0

for i in range(n):
    cursum+=a[i]
    if cursum==k:
        res+=1
    
    if (cursum-k) in prevSum:
        res+=prevSum[cursum-k]

    prevSum[cursum]+=1

print(res)