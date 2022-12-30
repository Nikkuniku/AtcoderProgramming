n,m=map(int,input().split())
V=n
edge=[set() for _ in range(n+1)]
indegree=[0]*(V+1)

for _ in range(m):
    k=int(input())
    a=list(map(int,input().split()))

    for i in range(k-1):
        p=a[i]
        q=a[i+1]
        if q not in edge[p]:
            indegree[q]+=1
        edge[p].add(q)
import heapq
q=[]
heapq.heapify(q)
ans=[]
for v in range(1,V+1):
    if indegree[v]==0:
        heapq.heappush(q,v)
while q:
    v=heapq.heappop(q)

    for e in list(edge[v]):
        indegree[e]-=1
        if indegree[e]==0:
            heapq.heappush(q,e)
    
    ans.append(v)

if len(ans)==V:
    print('Yes')
else:
    print('No')