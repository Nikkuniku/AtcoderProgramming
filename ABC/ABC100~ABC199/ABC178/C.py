n=int(input())

if n==1:
    print(0)
    exit(0)

mod = (10**9) +7

ans=pow(10,n,mod)

a=pow(9,n,mod)
b=pow(8,n,mod)

ans=(ans-2*a+b)%mod

print(ans)