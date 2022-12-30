n=int(input())
from collections import defaultdict
d_l=defaultdict(list)
d_r=defaultdict(list)
v=[]
for i in range(n):
    x,y=map(int,input().split())
    v.append((i,x,y))
s=list(input())

for i in range(n):
    w=v[i]
    if s[w[0]]=='R':
        d_r[w[2]].append(w[1])
    else:
        d_l[w[2]].append(w[1])

ans='No'
for c in list(d_l.items()):
    y=c[0]
    x_max=max(c[1])
    if d_r[y]:
        x_min=min(d_r[y])
    
        if x_min<=x_max:
            ans='Yes'

print(ans)