n=int(input())
a=list(map(int,input().split()))

mod=10**9+7
total = sum(a)
cum=[]

ans=0
for i in range(n):
    total-=a[i]
    ans += a[i]*(total)%mod
    

print(ans%mod)