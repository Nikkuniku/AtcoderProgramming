n,k=map(int,input().split())
p=list(map(int,input().split()))
import heapq
q=[]
heapq.heapify(q)

for j in range(n):
    a=p[j]
    heapq.heappush(q,a)
    if len(q)>k:
        heapq.heappop(q)
    if len(q)==k:
        ans=q[0]
        print(ans)