n,m=map(int,input().split())
a=list(map(int,input().split()))
l=max(a)
hurui=[0]*(l+1)
for b in a:
    hurui[b]+=1
divisor=set()
for i in range(2,l+1):
    add=i
    while i<=l:
        if hurui[i]>0:
            divisor.add(add)
        i+=add
dp=[0]*(m+1)
for k in list(divisor):
    t=k
    while k<=m:
        dp[k]+=1
        k+=t
ans=[]
for l in range(1,m+1):
    if dp[l]==0:
        ans.append(l)

print(len(ans))
print(*ans,sep="\n")