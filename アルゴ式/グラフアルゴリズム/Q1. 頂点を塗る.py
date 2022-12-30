N,M=map(int,input().split())
Edge=[[] for _ in range(N)]
for _ in range(M):
    a,b=map(int,input().split())
    Edge[a].append(b)
    Edge[b].append(a)

ans=[[] for _ in range(N)]
from collections import deque
q=deque([0])
seen=[False]*N
seen[0]=True
tmp=deque()
for k in range(N):
    if k==0:
        ans[k].append(0)
        continue
    while q:
        v=q.popleft()
        for e in Edge[v]:
            if not seen[e]:
                ans[k].append(e)
                tmp.append(e)
                seen[e]=True
    
    q,tmp=tmp,deque()

for c in ans:
    print(*sorted(c))
    