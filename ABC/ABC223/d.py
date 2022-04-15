V,E=map(int,input().split())
import heapq
edge=[[] for _ in range(V+1)]
indegree=[0]*(V+1)
inputs=set()
for _ in range(E):
    a,b=map(int,input().split())
    inputs.add((a,b))
inputs=list(inputs)
for c in inputs:
    a,b=c
    edge[a].append(b)
    indegree[b]+=1

q=[]
heapq.heapify(q)
ans=[]
for v in range(1,V+1):
    if indegree[v]==0:
        heapq.heappush(q,v)

while q:
    v=heapq.heappop(q)

    for e in edge[v]:
        indegree[e]-=1
        if indegree[e]==0:
            heapq.heappush(q,e)
    
    ans.append(v)

if len(ans)==V:
    print(*ans)
else:
    print(-1)