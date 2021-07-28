a,b,c=map(int,input().split())

d2=c-b
d1=b-a

ans=abs(d2-d1)


if d2-d1>=0:
    if (d2-d1)%2==0:
        ans=(d2-d1)//2
    else:
        ans=(d2-d1+1)//2 +1

print(ans)