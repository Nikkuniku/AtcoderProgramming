n,t=map(int,input().split())
a=list(map(int,input().split()))

a1=a[:len(a)//2]
a2=a[len(a)//2:]

w1=[]
w2=[]
for i in range(2**len(a1)):
    cost = 0
    for j in range(len(a1)):
        if ((i>>j) & 1):
            cost+=a1[j]
    if cost > t:
        continue

    w1.append(cost)

for i in range(2**len(a2)):
    cost = 0
    for j in range(len(a2)):
        if ((i>>j) & 1):
            cost+=a2[j]

    if cost > t:
        continue
    
    w2.append(cost)

w2=sorted(w2)

from bisect import bisect_right as br

ans=0
for i in range(len(w1)):
    if w1[i]>t:
        continue
    index = br(w2,t-w1[i])
    tar = w2[index-1]
    if tar+w1[i]>t:
        continue
    ans = max(ans,tar+w1[i])

print(ans)
