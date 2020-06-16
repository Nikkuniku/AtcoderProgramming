n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))



if sum(a)<sum(b):
    print(-1)
    exit(0)

dif=0
cnt=0
asis=0
#足りない項には足してあげる
for i in range(n):
    if a[i]<b[i]:
        dif-=(b[i]-a[i])
        a[i]=b[i]
        cnt+=1

if cnt==0:
    print(0)
    exit(0)

c=[]
for j in range(n):
    c.append(a[j]-b[j])

c=sorted(c,reverse=True)

#余裕があるところから引いていく
for k in range(n):
    if c[k]>=dif:
        dif+=c[k]
        cnt+=1

    if dif>=0:
        break

print(cnt)