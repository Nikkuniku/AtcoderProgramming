n,k=map(int,input().split())
a=list(map(int,input().split()))
mod=1000_000_000+7
l=[0]*n
r=[0]*n
total=[0]*n
for i in range(n):
    for j in range(n):
        if a[i]>a[j]:
            if i>=j:
                l[i]+=1
            else:
                r[i]+=1
            total[i]+=1


ans=0

for i in range(n):
    ans+=(total[i]*k*(k+1))//2 
    ans-=k*l[i]

print(ans%mod)