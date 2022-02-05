n,x,y=map(int,input().split())

ans='No'
p=abs(x)+abs(y)
if p<=n:
    if p%2 ==n%2:
        ans='Yes'

print(ans)