k=int(input())
s=input()
n=len(s)

mod=1_000_000_000+7
p=n+1+k

ans=pow(26,p+1)%mod

print(ans)