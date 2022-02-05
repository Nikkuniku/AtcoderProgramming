n=int(input())
p=1000000007

m=n+1
if n+1>=p-1:
    m=(n+1)%(p-1)

a=pow(4,m,p)*pow(3,p-2,p)
b=pow(3,p-2,p)
a%=p
b%=p

ans=(a-b)%p
print(ans)