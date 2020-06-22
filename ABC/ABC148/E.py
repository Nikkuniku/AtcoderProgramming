n=int(input())
if n%2==1:
    print(0)
    exit(0)

n//=2
from math import floor,factorial

ans=0
deno=5
while deno<=n:
    ans+=n//deno
    deno*=5

print(ans)