n,m=map(int,input().split())
a=[0]
for _ in range(n):
    a.append(int(input()))


w=[]

for i in range(n+1):
    for j in range(i,n+1):
        w.append(a[i]+a[j])

w=sorted(w)
from bisect import bisect_right

ans=0
p=[]
for k in range(len(w)):
    base = m-w[k]
    index= bisect_right(w,m-w[k])
    tar = w[index-1]
    if w[k] + tar >m:
        continue
    p.append(w[k]+tar)
    ans = max(ans,w[k]+tar)

print(ans)


