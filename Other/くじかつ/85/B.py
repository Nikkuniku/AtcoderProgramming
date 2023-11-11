n=int(input())
a=list(map(int,input().split()))

mod=10**9+7

s=sum(a)%mod

ans=0
for i in range(n-1):
    s=(s-a[i])%mod
    ans=(ans + a[i]*s)%mod

print(ans)