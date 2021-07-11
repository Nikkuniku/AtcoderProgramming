n=int(input())
c=list(map(int,input().split()))
mod=10**9 + 7 
ans=1
c=sorted(c)

for i in range(n):
    ans=ans*max(0,c[i]-i)%mod

print(ans%mod)