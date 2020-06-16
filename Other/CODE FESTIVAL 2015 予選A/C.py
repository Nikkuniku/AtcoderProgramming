n,t=map(int,input().split())

d=[]
al=0
for _ in range(n):
    a,b=map(int,input().split())

    d.append(b-a)
    al+=a
d=sorted(d)


cnt=0
j=0
for i in range(n):
    if al>t:
        al+=d[j]
        j+=1
        cnt+=1
    else:
        break

if al>t:
    print(-1)
else:
    print(cnt)