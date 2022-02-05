n=int(input())
a=list(map(int,input().split()))
mod=1000000007
ans=0
for i in range(n):
    ans+=(a[i]%mod)*pow(2,i,mod)
    ans%=mod
print(ans)