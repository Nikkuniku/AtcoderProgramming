a,b,c=map(int,input().split())

ans='='
if c%2==0:
    a=abs(a)
    b=abs(b)

if a>b:
    ans='>'
elif a<b:
    ans='<'

print(ans)