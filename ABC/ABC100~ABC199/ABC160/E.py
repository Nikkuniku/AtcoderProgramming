x,y,a,b,c=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=list(map(int,input().split()))

p=sorted(p,reverse=True)
q=sorted(q,reverse=True)
r=sorted(r)
p=p[:x]
q=q[:y]

import heapq
from collections import deque

heapq.heapify(p)
heapq.heapify(q)
r=deque(r)

for i in range(c):
    v_p=heapq.heappop(p)
    v_q=heapq.heappop(q)

    v_r=r.pop()
    if v_p<=v_q:
        heapq.heappush(q,v_q)
        if v_p<v_r:
            heapq.heappush(p,v_r)
        else:
            heapq.heappush(p,v_p)
    else:
        heapq.heappush(p,v_p)
        if v_q<v_r:
            heapq.heappush(q,v_r)
        else:
            heapq.heappush(q,v_q)

ans=sum(p)+sum(q)

print(ans)