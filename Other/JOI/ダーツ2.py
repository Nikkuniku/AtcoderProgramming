n,m=map(int,input().split())
p=[]
for _ in range(n):
    p.append(int(input()))

w1=[0]+p

for i in range(n):
    for j in range(i,n):
        w1.append(p[i]+p[j])

w2=sorted(w1.copy())

import bisect

ans=0
for w in w1:
    if w>m:
        continue
    index = bisect.bisect_right(w2,m-w)

    ans=max(ans,w2[index-1]+w)

print(ans)
