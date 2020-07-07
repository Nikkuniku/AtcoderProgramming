n=int(input())
a=list(map(int,input().split()))
mod=10**9+7

a=sorted(a)
flgs=[]
if n%2==0:
    k=n//2
    for i in range(1,k+1):
        flgs.append(2*i-1)
        flgs.append(2*i-1)
else:
    k=(n-1)//2
    flgs.append(0)
    for j in range(1,k+1):
        flgs.append(2*j)
        flgs.append(2*j)

flgs=sorted(flgs)
if flgs==a:
    ans=2**k
    print(ans%mod)
else:
    print(0)