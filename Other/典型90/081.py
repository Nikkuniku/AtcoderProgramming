n,k=map(int,input().split())
from collections import deque
h=[]
for i in range(n):
    a,b=map(int,input().split())
    h.append([a,b,i+1])
q=deque()
h=sorted(h,key=lambda x:x[0])

cnt=1
for a in h:
    q.append(a)
    q_min=q[0]
    q_max=q[-1]
    
    while q and abs(q_max-q_min)>k:
        rm=q.popleft()