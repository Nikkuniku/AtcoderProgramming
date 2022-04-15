n=int(input())
a=list(map(int,input().split()))
d0={0:1,1:-1}
d1={0:-1,1:1}
cur=0
zeroplus=-10**18
for i in range(n):
    cur =max(d0[a[i]],d0[a[i]]+cur)
    zeroplus=max(zeroplus,cur)
cur=0
oneminus=-10**18
for i in range(n):
    cur=max(d1[a[i]],d1[a[i]]+cur)
    oneminus=max(oneminus,cur)
zeroplus=max(0,zeroplus)
oneminus=max(0,oneminus)
ans=zeroplus+oneminus+1
print(ans)