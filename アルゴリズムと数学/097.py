L,R=map(int,input().split())

rl=[True]*(R-L+1)
if L==1:
    rl[0]=False
k=L
for i in range(2,int(R**0.5)+1):
    if L%i==0:
        s=L
    else:
        s=L+i-(L%i)
    j=i
    while s<R+1:
        if s!=i:
            rl[s-L]=False
        s+=j

ans=0
for k in range(len(rl)):
    if rl[k]:
        ans+=1
print(ans)