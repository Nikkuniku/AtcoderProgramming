x,y,a,b = map(int,input().split())

# 大きくなるnを見つける
n=0
ans=0
while (a**n)*x <y:
    p = ( y - (a**n)*x )//b
    if ( y - (a**n)*x )%b ==0:
        p-=1

    ans = max(ans,n+p)
    n+=1
    z=y - (a**n)*x


print(ans)