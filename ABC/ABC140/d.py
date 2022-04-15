n,K=map(int,input().split())
s=input()
s=s.replace('L','0')
s=s.replace('R','1')
s=list(map(int,s))
from itertools import groupby
from collections import deque
gr=groupby(s)
col=[]
for key,value in gr:
    col.append([key,len(list(value)),0,0])
for i in range(1,len(col)):
    col[i][2]+=col[i-1][1]+col[i-1][2]
for j in range(len(col)):
    col[j][3]=col[j][2]+col[j][1]-1
csum=[0]
for k in range(1,len(s)):
    p=csum[-1]
    if s[k-1]==s[k]:
        p+=1
    csum.append(p)
q=deque([])
ans=0
now=0
for i in range(len(col)):
    p=col[i]
    c=p[1]
    q.append(p)
    now+=c
    if len(q)>2*K +1:
        v=q.popleft()
        now-=v[1]
    tmp=csum[q[0][2]]+now-1+(csum[-1]-csum[q[-1][3]])
    ans=max(ans,tmp)
print(ans)