n,k=map(int,input().split())

deno=n**3

ans=1+3*(n-1)
if k!=1 and k!=n:
    ans+=6*(k-1)*(n-k)

print(ans/deno)