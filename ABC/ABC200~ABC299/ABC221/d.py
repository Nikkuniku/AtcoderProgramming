n=int(input())
from collections import defaultdict
d=defaultdict(lambda:0)

for _ in range(n):
    a,b=map(int,input().split())
    d[a]+=1
    d[a+b]-=1

p=list(d.items())
q=[]
for c in p:
    q.append([c[0],c[1]])
q=sorted(q,key=lambda x:x[0])
for j in range(1,len(q)):
    q[j][1]+=q[j-1][1]

ans=defaultdict(int)

for k in range(len(q)-1):
    m=q[k][1]
    ans[m]+=q[k+1][0]-q[k][0]

answer=[]
for k in range(1,n+1):
    answer.append(ans[k])
print(*answer)