a,b,c,x=map(int,input().split())

ans=0
if x<=a:
    ans=1
elif a<x<=b:
    ans=c/(b-a)

print(ans)