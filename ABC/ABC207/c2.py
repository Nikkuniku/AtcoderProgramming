n=int(input())
segment=[]
for _ in range(n):
    t,l,r=map(int,input().split())
    if t==1:
        pass
    elif t==2:
        r-=0.5
    elif t==3:
        l+=0.5
    else:
        l+=0.5
        r-=0.5
    segment.append([l,r])

ans=0
for i in range(n):
    for j in range(i+1,n):
        p=segment[i]
        q=segment[j]

        if max(p[0],q[0])<=min(p[1],q[1]):
            ans+=1

print(ans)