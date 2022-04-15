n,k=map(int,input().split())
pre=0
diff=[]
for i in range(n):
    a=int(input())
    if i!=0:
        f=0
        if pre<a:
            f=1
        diff.append(f)
    pre=a
from collections import defaultdict,deque
d=defaultdict(int)
q=deque([])
ans=0
for i in range(len(diff)):
    v=diff[i]
    q.append(v)
    d[v]+=1
    if len(q)>k-1:
        w=q.popleft()
        d[w]-=1
    
    if len(q)==k-1:
        if d[0]==0:
            ans+=1
if k==1:
    ans=n
print(ans)