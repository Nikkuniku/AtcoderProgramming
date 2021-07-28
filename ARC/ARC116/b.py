from sys import stdin

n=int(input())
a=list(map(int,stdin.readline().split()))
mod=998244353
a=sorted(a)

ans=0
if n==1:
    print(pow(a[0],2,mod))
    exit(0)


for i in range(n):
    ans = ( ans + pow(a[i],2,mod) )%mod

s=0 
for i in range(n-1,-1,-1):
    ans = (ans + s*a[i])%mod
    s =(2*s + a[i])%mod

print(ans%mod)